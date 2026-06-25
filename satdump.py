import requests
import pandas as pd
import time

def fetch_all_pages(url, description):
    results = []
    current_url = url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    print(f"-> Downloading {description}...", end="", flush=True)
    
    while current_url:
        try:
            response = requests.get(current_url, headers=headers, timeout=20)
            response.raise_for_status()
            data = response.json()
            
            if isinstance(data, dict) and 'results' in data:
                results.extend(data['results'])
                current_url = data.get('next')
            elif isinstance(data, list):
                results.extend(data)
                current_url = None
            else:
                current_url = None
                
            print(".", end="", flush=True)
            time.sleep(0.01)
            
        except Exception as e:
            print(f"\n[ERROR] Failed during download: {e}")
            break
            
    print(f" Done! (Total items: {len(results)})")
    return results

def download_amateur_repeaters():
    print("=== SatNOGS DB Data Fetcher ===")
    
    sat_url = "https://db.satnogs.org/api/satellites/?format=json"
    trans_url = "https://db.satnogs.org/api/transmitters/?format=json"
    
    satellites = fetch_all_pages(sat_url, "satellite names")
    transmitters = fetch_all_pages(trans_url, "transmitters")
    
    if not transmitters:
        print("Failed to get transmitter data.")
        return

    # Το SatNOGS satellites API επιστρέφει συνήθως το norad_cat_id
    sat_mapping = {}
    for sat in satellites:
        s_id = str(sat.get('norad_cat_id', sat.get('sat_id', '')))
        if s_id and s_id != 'None':
            sat_mapping[s_id] = sat.get('name', 'Unknown')

    repeater_data = []

    for item in transmitters:
        # Φίλτρο για active
        status = str(item.get('status', '')).lower().strip()
        if status != "active":
            continue

        # ΤΑ ΣΩΣΤΑ ΚΛΕΙΔΙΑ ΤΟΥ API:
        norad_id = str(item.get('norad_cat_id', item.get('norad_follow_id', '')))
        if not norad_id or norad_id == 'None':
            continue
            
        down_freq_raw = item.get('downlink_low')
        up_freq_raw = item.get('uplink_low')
        
        if down_freq_raw is None and up_freq_raw is None:
            continue
            
        try:
            down_mhz = f"{float(down_freq_raw) / 1e6:.4f}" if down_freq_raw else "N/A"
        except (ValueError, TypeError):
            down_mhz = "N/A"
            
        try:
            up_mhz = f"{float(up_freq_raw) / 1e6:.4f}" if up_freq_raw else "N/A"
        except (ValueError, TypeError):
            up_mhz = "N/A"
            
        if down_mhz == "N/A" and up_mhz == "N/A":
            continue
        
        sat_name = sat_mapping.get(norad_id, "Unknown Satellite")
        
        repeater_data.append({
            "NORAD ID": norad_id,
            "Satellite Name": sat_name,
            "Type": item.get('type', 'N/A'),
            "Mode": item.get('mode', 'N/A'),
            "Downlink (MHz)": down_mhz,
            "Uplink (MHz)": up_mhz,
            "Inverted": item.get('invert', False)
        })

    if not repeater_data:
        print("Filter mismatch. No active repeaters matched.")
        # ΑΣΦΑΛΙΣΤΙΚΗ ΔΙΚΛΕΙΔΑ: Αν κάτι πάει στραβά, θα δεις το πραγματικό JSON
        if transmitters:
            print("\n[DEBUG] Το API άλλαξε πεδία. Δες πώς μοιάζει πραγματικά μια ωμή εγγραφή:")
            print(transmitters[0])
        return

    df = pd.DataFrame(repeater_data)
    df = df.sort_values(by="Satellite Name")

    output_file = "amateur_satellite_repeaters.csv"
    df.to_csv(output_file, index=False)
    
    print(f"\n[SUCCESS] Extracted {len(df)} active repeaters/transmitters.")
    print(f"Saved to: '{output_file}'")
    
    print("\nData Sample:")
    print(df[["NORAD ID", "Satellite Name", "Type", "Downlink (MHz)", "Uplink (MHz)"]].head(10).to_string(index=False))

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

if __name__ == "__main__":
    download_amateur_repeaters()