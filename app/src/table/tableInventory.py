from config.configdb import db

class Inventory(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(60))
  price = db.Column(db.Integer)
  mac_address = db.Column(db.String(17)) #xx:xx:xx:xx:xx:xx 
  serial_number = db.Column(db.String(30)) 
  manufacture = db.Column(db.String(30)) 
  description = db.Column(db.String(300))

  def __init__(self, name, price, mac_address, serial_number, manufacturer, description):
    self.name = name
    self.price = price
    self.mac_address = mac_address
    self.serial_number = serial_number
    self.manufacturer = manufacturer
    self.description = description
