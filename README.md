# SatNOGS Dumper

A Python tool for extracting active satellite repeater data from the SatNOGS DB.

## Prerequisites

You need Python 3 and the following libraries:

```bash
pip install requests pandas
```

## Usage
Clone the repository:

```bash
git clone https://github.com/z1000biker/satnogsdump
cd satnogsdump
```

Execute the script:

```bash
python gemini-code-1782418973676.py
```

The file amateur_satellite_repeaters.csv will be created automatically in the project folder.

## CSV Structure
NORAD ID: Satellite identification code.

Satellite Name: The name of the satellite.

Type: Transmitter type.

Mode: Operating mode.

Downlink (MHz): Downlink frequency.

Uplink (MHz): Uplink frequency.

Inverted: Indicates if the transponder is inverting.

## Technical Notes
The script connects to the official SatNOGS DB API endpoints:

https://db.satnogs.org/api/satellites/

https://db.satnogs.org/api/transmitters/

## License
Free to use for the amateur radio community.

SatNOGS Dumper
Εργαλείο Python για την εξαγωγή δεδομένων ενεργών δορυφορικών αναμεταδοτών από τη βάση δεδομένων του SatNOGS DB.

## Προαπαιτούμενα
Χρειάζεσαι την Python 3 και τις παρακάτω βιβλιοθήκες:

```bash
pip install requests pandas
```

## Χρήση
Κάνε clone το repository:

```bash
git clone https://github.com/z1000biker/satnogsdump
cd satnogsdump
```

Εκτέλεσε το script:

```bash
python gemini-code-1782418973676.py
```

Το αρχείο amateur_satellite_repeaters.csv θα δημιουργηθεί αυτόματα στον φάκελο του project.

## Δομή CSV
NORAD ID: Κωδικός ταυτοποίησης δορυφόρου.

Satellite Name: Το όνομα του δορυφόρου.

Type: Τύπος πομπού.

Mode: Mode λειτουργίας.

Downlink (MHz): Συχνότητα λήψης.

Uplink (MHz): Συχνότητα εκπομπής.

Inverted: Ένδειξη αν ο αναμεταδότης είναι inverting.

## Τεχνικές Σημειώσεις
Το script συνδέεται στα επίσημα API endpoints του SatNOGS DB:

https://db.satnogs.org/api/satellites/

https://db.satnogs.org/api/transmitters/

## License
Δωρεάν για χρήση από την κοινότητα των ραδιοερασιτεχνών.
