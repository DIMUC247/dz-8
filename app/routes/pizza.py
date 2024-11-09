from flask import Blueprint,render_template,request,redirect,flash
from app.db.__init import Session,Pizza
from app.data.password import ADMIN_PASS


pizza_route = Blueprint("pizza", __name__)


# @pizza_route.get("/")
# @pizza_route.post("/")
# def add_pizza():
#     block = False
#     msg = ""
#     with Session() as session:
#         if request.method == "post":
#             name = request.form.get("name")
#             price = request.form.get("price")

#             if request.form.get("password") == ADMIN_PASS:
#                 pizza = Pizza(name=name,price=price)
#                 session.add(pizza)
#                 session.commit()
#                 msg = "піццу уcпішно додано"
#             else:
#                 block = True
#         pizzas = session.query(Pizza).all()
#         context = {
#             "pizzas": pizzas,
#             "block": block,
#             "msg": msg
#         }
#         return render_template("pizza.html",**context)


@pizza_route.get("/pizzas/")
@pizza_route.post("/pizzas/")
def add_pizza():
     with Session() as session:
        if request.method == "POST":
            name = request.form.get("name")
            price = request.form.get("price")
            pizza = Pizza(name=name,price=price)

            if request.form.get("password") == ADMIN_PASS:
                session.add(name)
                session.commit()
                flash("Піццу успішно додано")
            else:
                flash("Нeвийшло додати піцу")

        pizza = session.query(Pizza).all()
        return render_template("add_pizza.html", pizza=pizza)
