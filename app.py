from flask import Flask, jsonify, request
from models import db, Vendor, Sweet, Order, OrderItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vendor_sweets.db'
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/vendors', methods=['GET'])
def get_vendors():
    vendors = Vendor.query.all()
    data = [{'id': vendor.id, 'name': vendor.name} for vendor in vendors]
    return jsonify(data)


@app.route('/vendors', methods=['POST'])
def create_vendor():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    vendor = Vendor(name=name)
    db.session.add(vendor)
    db.session.commit()

    return jsonify({'id': vendor.id, 'name': vendor.name}), 201

@app.route('/vendors/<int:id>', methods=['PUT'])
def update_vendor(id):
    vendor = Vendor.query.get(id)

    if not vendor:
        return jsonify({'error': 'Vendor not found'}), 404

    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    vendor.name = name
    db.session.commit()

    return jsonify({'id': vendor.id, 'name': vendor.name}), 200

@app.route('/vendors/<int:id>', methods=['DELETE'])
def delete_vendor(id):
    vendor = Vendor.query.get(id)

    if not vendor:
        return jsonify({'error': 'Vendor not found'}), 404

    db.session.delete(vendor)
    db.session.commit()

    return '', 204
# Routes for Sweets
@app.route('/sweets', methods=['GET'])
def get_sweets():
    sweets = Sweet.query.all()
    data = [{'id': sweet.id, 'name': sweet.name, 'price': sweet.price, 'vendor_id': sweet.vendor_id} for sweet in sweets]
    return jsonify(data)

@app.route('/sweets', methods=['POST'])
def create_sweet():
    data = request.json
    name = data.get('name')
    price = data.get('price')
    vendor_id = data.get('vendor_id')

    if not all([name, price, vendor_id]):
        return jsonify({'error': 'Name, price, and vendor_id are required'}), 400

    sweet = Sweet(name=name, price=price, vendor_id=vendor_id)
    db.session.add(sweet)
    db.session.commit()

    return jsonify({'id': sweet.id, 'name': sweet.name, 'price': sweet.price, 'vendor_id': sweet.vendor_id}), 201


if __name__ == '__main__':
    app.run(debug=True)
