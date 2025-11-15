from flask import Flask, render_template

#  step 1 to cretae flask app
app = Flask(__name__)

# step 2 homepage route
@app.route("/")
def home():
    return render_template("index.html")

# step 3 product page
@app.route("/products")
def products():
    grocery_items = [
        {"name": "Apples", "price": "₹120/kg", "image": "apple.jpeg.jpeg"},
        {"name": "Bananas", "price": "₹60/dozen", "image": "banana.jpeg.jpeg"},
        {"name": "Tomatoes", "price": "₹40/kg", "image": "tomato.jpeg.jpeg"},
        {"name": "Milk", "price": "₹55/litre", "image": "milk.jpeg.jpeg"},
        {"name": "Rice", "price": "₹80/kg", "image": "rice.jpeg.jpeg"}
    ]
    return render_template("products.html", items=grocery_items)

# Step 4: Contact page
@app.route("/contact")
def contact():
    contact_info = [
        {"type": "Phone", "value": "+91-9876543210"},
        {"type": "Email", "value": "grocery@example.com"},
        {"type": "WhatsApp", "value": "+91-9123456789"},
        {"type": "Address", "value": "123 Market Road, Pune"}
    ]
    return render_template("contact.html", contacts=contact_info)

# Step 5: Run the app
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

