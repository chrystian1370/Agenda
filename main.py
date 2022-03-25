from flask import Flask, render_template, request, redirect
app = Flask('app')

contacts = [
  {'name' : 'Chrystian Alvarenga' },  
]

@app.route('/')
def index():
  return render_template(
    'index.html',
    contacts=contacts
  )

@app.route('/create', methods=['POST'])
def create():
  title = request.form.get('name')
  contacts.append({'name':title})
  return redirect ('/')
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)