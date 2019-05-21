#prerequisites
from flask import Flask, render_template, request
from requests import get
app = Flask(__name__)
app.debug = False
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
#currency conversion function
def currency_converter(value,base_currency,output_currency):
    return round(get('https://api.exchangeratesapi.io/latest', params = {'symbols': output_currency, 'base': base_currency}).json()['rates'][output_currency]*value,2)

#start code:
@app.route('/', methods=['GET','POST'])
def converter():
    currencies = ['ISK','CAD','MXN','CHF','AUD','CNY','GBP','USD','SEK','NOK','TRY','IDR','ZAR','HRK','EUR','HKD','ILS','NZD','MYR','JPY','CZK','SGD','RUB','RON','HUF','BGN','INR','KRW','DKK','THB','PHP','PLN','BRL']
    if request.args.get('value')==None:
        value = ""
    else:
        value = request.args.get('value')
    if request.args.get('base_currency')==None or request.args.get('base_currency')=="":
        base_currency = ""
    else:
        base_currency = request.args.get('base_currency')
    if request.args.get('output_currency')==None:
        output_currency = ""
    else:
        output_currency = request.args.get('output_currency')
    if value=="" or output_currency=="" or base_currency=="" or is_number(value)==False:
        return render_template('index.html', currencies=currencies, value=value, base_currency=base_currency, output_currency=output_currency)
    else:
        end = str(currency_converter(float(request.args.get('value')),request.args.get('base_currency'),request.args.get('output_currency')))
        return render_template('index.html', end=end, currencies=currencies, value=value, base_currency=base_currency, output_currency=output_currency)
if __name__ == "__main__":
    app.run()
