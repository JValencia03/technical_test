from flask import render_template, Blueprint, redirect, request, flash
from table.tableInventory import Inventory
from config.configdb import db

techTest = Blueprint('techTest', __name__)

@techTest.route('/')
def reading():
  inventory = Inventory.query.all()
  return render_template('add.html', inventory = inventory)

@techTest.route('/add', methods=['POST'])
def create():
  name = request.form['name']
  price = request.form['price']
  macAddress = request.form['mac_address']
  serialNumber = request.form['serial_number']
  manufacture = request.form['manufacture']
  description = request.form['description']

  newElement = Inventory(name, price, macAddress, serialNumber, manufacture, description)

  db.session.add(newElement)

  db.session.commit()

  flash('New element added')

  return redirect('/')

@techTest.route('/edit/<id>', methods = ['GET', 'POST'])
def updating(id):
  inventory = Inventory.query.get(id)

  if request.method == 'POST':    
    inventory.name = request.form['name']
    inventory.price = request.form['price']
    inventory.macAddress = request.form['mac_address']
    inventory.serialNumber = request.form['serial_number']
    inventory.manufacture = request.form['manufacture']
    inventory.description = request.form['description']

    db.session.commit()

    return redirect('/')

  return render_template('updating.html', inventory = inventory)

@techTest.route('/delete/<id>')
def deleting(id):
  inventory = Inventory.query.get(id)
  db.session.delete(inventory)
  db.session.commit()

  return redirect('/')
