from .forms import *
from .models import *
from flask import render_template, flash, url_for, redirect

@app.route('/signup',methods=['GET', 'POST'])
def signup1():
    form = signup()
    if form.validate_on_submit():
        if form.password.data != form.conpassword.data:
            flash('Password mush match!')
        else:
            new_user = Customer(username=form.username.data,
                                firstName=form.firstname.data,
                                lastName=form.lastname.data,
                                email=form.email.data,
                                password=form.password.data,
                                address=form.address.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template("Signup.html", form=form)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/menu', methods=['GET', 'POST'])
def menu():

    form0 = menu1(prefix='form0')
    form1 = menu1(prefix='form1')
    form2 = menu1(prefix='form2')

    list = [form0,form1,form2]

    # number = [
    #     '1.Cheeseburger','2.Rice','3.Doge','4.Indo Coca Cola','5.Waifu'
    # ]
    # itemdes = [
    #     'Cheap Ass Burger', 'If you are Asian, get this', 'Animal abuse? Call PETA!', 'Limited time Coca Cola from Indo!',
    #     'Nier Automata 2B'
    # ]
    # price = [
    #     1.00,2.00, 100.00, 3.00, 500.00
    # ]
    total = [0]

    validate = True
    for i in list:
        validate = validate and i.validate_on_submit()
    #if (list[0].validate_on_submit() and list[0].qty.data and list[1].validate_on_submit() and list[1].qty.data and list[2].validate_on_submit() and list[2].qty.data):
    # if form2.validate_on_submit():
    if validate:
        print(form0.qty.data)
        print(form1.qty.data)
        print(form2.qty.data)

        return '<h1>' + str(list[0].qty.data) + ' ' + str(list[1].qty.data) + ' '+ str(list[2].qty.data) + '</h1>'
        #return redirect(url_for('contact'))
        # return render_template("checkout.html", total=total)
    return render_template("menu.html", formlist=list, fooditems = FoodItems.query.all())
                           # total=total, number=number, itemdes=itemdes, price=price, iterr=zip(number,itemdes,price),
                           # databaseitems = Menu.query.all())

@app.route('/checkout')
def check():

    return render_template("checkout.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = login1()
    if form.validate_on_submit():

        customer = Customer.query.filter_by(username=form.username.data).first()
        if customer:
            if customer.password == form.password.data:
                return redirect(url_for('contact'))
            else:
                flash('Incorrect password or email')
    return render_template("login.html", form=form)

@app.route('/contact')
def contact():
    return render_template("contact.html")