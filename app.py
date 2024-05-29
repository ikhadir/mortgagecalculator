from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_mortgage(loan_amount, interest_rate, loan_term):
    P = loan_amount
    r = interest_rate / 12
    n = loan_term * 12
    x = (r * P * (1 + r) ** n) / (-1 + (1 + r) ** n)
    return x

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        loan_amount = float(request.form['loan_amount'])
        interest_rate = float(request.form['interest_rate']) / 100  # Convert percentage to decimal
        loan_term = int(request.form['loan_term'])
        
        monthly_payment = calculate_mortgage(loan_amount, interest_rate, loan_term)
        
        return render_template('index.html', monthly_payment=monthly_payment)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
