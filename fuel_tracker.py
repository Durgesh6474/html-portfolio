import json
import os
from datetime import datetime
import argparse

DATA_FILE = 'fuel_data.json'
VEHICLE_COUNT = 70


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    # Initialize data structure with vehicles
    data = {
        'vehicles': {str(i): {'fuel_events': []} for i in range(1, VEHICLE_COUNT + 1)}
    }
    return data


def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def add_fuel(vehicle_id, amount):
    data = load_data()
    vehicle = data['vehicles'].get(str(vehicle_id))
    if vehicle is None:
        print(f"Vehicle {vehicle_id} does not exist")
        return
    vehicle['fuel_events'].append({
        'date': datetime.now().isoformat(timespec='seconds'),
        'amount': amount
    })
    save_data(data)
    print(f"Added {amount} liters of fuel to vehicle {vehicle_id}.")


def report():
    data = load_data()
    for vid, info in data['vehicles'].items():
        total = sum(event['amount'] for event in info['fuel_events'])
        print(f"Vehicle {vid}: {total} liters total")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fuel Tracking System')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add fuel entry')
    add_parser.add_argument('vehicle_id', type=int, help='Vehicle ID (1-70)')
    add_parser.add_argument('amount', type=float, help='Fuel amount in liters')

    subparsers.add_parser('report', help='Show fuel usage report')

    args = parser.parse_args()
    if args.command == 'add':
        add_fuel(args.vehicle_id, args.amount)
    elif args.command == 'report':
        report()
    else:
        parser.print_help()
