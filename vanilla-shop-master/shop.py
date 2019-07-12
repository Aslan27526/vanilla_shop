from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser='postgres',
    dbpass='lobato9090',
    dbhost='localhost',
    dbname='vanilla_shop'
)

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
db = SQLAlchemy(app)


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    price = db.Column(db.Float)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return name


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), nullable=False)
    customer_name = db.Column(db.String(200))

    def __init__(self, product_id, customer_name):
        self.product_id = product_id
        self.customer_name = customer_name


db.create_all()


@app.route('/')
def index():
    products = Product.query.order_by(Product.id).all()
    return render_template('index.html', products=products)


@app.route('/run')
def run():
    db.create_all()
    return 0


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form["price"]

        product = Product(name, price)
        db.session.add(product)
        db.session.commit()

        return "{} - {}". format(name, price)
    return render_template('create.html')
@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    product = Product.query.get(id)
    if request.method=='POST':
        product.name = request.form['name']
        product.price = request.form['price']
        db.session.commit()
        return " New name is {}".format(product.name)
    return render_template('edit.html/',product=product)
    