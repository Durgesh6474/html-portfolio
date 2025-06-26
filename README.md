# Municipal Council Fuel Tracking

This repository contains a simple command line application for tracking fuel usage for a municipal council fleet of 70 vehicles.

## Usage

```
python fuel_tracker.py add <vehicle_id> <amount>
```

Adds a fuel entry for the specified vehicle.

```
python fuel_tracker.py report
```

Prints the total fuel used for each vehicle.

Fuel data is stored locally in `fuel_data.json`.
