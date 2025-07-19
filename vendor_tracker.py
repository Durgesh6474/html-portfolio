import json
import os
from datetime import datetime
import argparse
import base64

DATA_FILE = 'vendor_data.json'


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {'vendors': {}}


def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def add_vendor(vendor_id, name, mobile, area, photo):
    data = load_data()
    if vendor_id in data['vendors']:
        print(f"Vendor {vendor_id} already exists")
        return
    data['vendors'][vendor_id] = {
        'name': name,
        'mobile': mobile,
        'area': area,
        'photo': photo,
        'taxes': [],
        'fines': []
    }
    save_data(data)
    print(f"Added vendor {vendor_id} - {name}")


def add_tax(vendor_id, amount):
    data = load_data()
    vendor = data['vendors'].get(vendor_id)
    if vendor is None:
        print(f"Vendor {vendor_id} not found")
        return
    vendor['taxes'].append({
        'date': datetime.now().isoformat(timespec='seconds'),
        'amount': amount
    })
    save_data(data)
    print(f"Added tax record for vendor {vendor_id}")


def add_fine(vendor_id, amount, reason):
    data = load_data()
    vendor = data['vendors'].get(vendor_id)
    if vendor is None:
        print(f"Vendor {vendor_id} not found")
        return
    vendor['fines'].append({
        'date': datetime.now().isoformat(timespec='seconds'),
        'amount': amount,
        'reason': reason
    })
    save_data(data)
    print(f"Added fine for vendor {vendor_id}")


def qr_string(vendor_id):
    data = load_data()
    vendor = data['vendors'].get(vendor_id)
    if vendor is None:
        print(f"Vendor {vendor_id} not found")
        return
    info = json.dumps({
        'id': vendor_id,
        'name': vendor['name'],
        'mobile': vendor['mobile'],
        'area': vendor['area']
    })
    encoded = base64.urlsafe_b64encode(info.encode()).decode()
    print(encoded)


def report():
    data = load_data()
    for vid, vinfo in data['vendors'].items():
        total_tax = sum(t['amount'] for t in vinfo['taxes'])
        total_fine = sum(f['amount'] for f in vinfo['fines'])
        print(f"Vendor {vid}: {vinfo['name']} - Area: {vinfo['area']} - Taxes: {total_tax} - Fines: {total_fine}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Street Vendor Management')
    sub = parser.add_subparsers(dest='command')

    av = sub.add_parser('add_vendor', help='Add a new vendor')
    av.add_argument('vendor_id')
    av.add_argument('name')
    av.add_argument('mobile')
    av.add_argument('area')
    av.add_argument('--photo', default='')

    tax = sub.add_parser('add_tax', help='Record tax payment')
    tax.add_argument('vendor_id')
    tax.add_argument('amount', type=float)

    fine = sub.add_parser('add_fine', help='Record fine')
    fine.add_argument('vendor_id')
    fine.add_argument('amount', type=float)
    fine.add_argument('reason')

    sub.add_parser('report', help='Show vendor report')

    qr = sub.add_parser('qr', help='Show vendor QR data string')
    qr.add_argument('vendor_id')

    args = parser.parse_args()
    if args.command == 'add_vendor':
        add_vendor(args.vendor_id, args.name, args.mobile, args.area, args.photo)
    elif args.command == 'add_tax':
        add_tax(args.vendor_id, args.amount)
    elif args.command == 'add_fine':
        add_fine(args.vendor_id, args.amount, args.reason)
    elif args.command == 'report':
        report()
    elif args.command == 'qr':
        qr_string(args.vendor_id)
    else:
        parser.print_help()
