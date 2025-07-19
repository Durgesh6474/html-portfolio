# Municipal Council Data Tools

This repository contains command line tools for municipal operations. The original tool `fuel_tracker.py` tracks fuel usage for a fleet of 70 vehicles.

A new tool `vendor_tracker.py` manages information about licensed street vendors, tax payments and fines.

## Fuel Tracker Usage

```bash
python fuel_tracker.py add <vehicle_id> <amount>
```
Adds a fuel entry for the specified vehicle.

```bash
python fuel_tracker.py report
```
Prints the total fuel used for each vehicle.
Fuel data is stored in `fuel_data.json`.

## Vendor Tracker Usage

```bash
python vendor_tracker.py add_vendor <id> <name> <mobile> <area> [--photo PATH]
```
Registers a new street vendor.

```bash
python vendor_tracker.py add_tax <id> <amount>
```
Records a tax payment for the vendor.

```bash
python vendor_tracker.py add_fine <id> <amount> <reason>
```
Records a spot fine for the vendor.

```bash
python vendor_tracker.py report
```
Shows a summary of vendors with total taxes and fines.

```bash
python vendor_tracker.py qr <id>
```
Prints a QR data string that encodes the vendor's basic information.

Vendor data is stored in `vendor_data.json`.
