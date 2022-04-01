from flask import Flask, render_template, request, redirect
app = Flask('app')

contacts = [
  { 
    'name': 'Chrystian Alvarenga',
    'email':'chrystianalvarenga@hotmail.com',
    'phone':'(16)99460-3667'    
  }
]

@app.route('/')
def index():
  return render_template('index.html',contacts=contacts)

@app.route('/create', methods=['POST'])
def create():
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  contacts.append({
    'name': name,   
    'email': email,
    'phone': phone
  })
  return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
  contacts.pop(index)
  return redirect('/')


@app.route('/update/<int:index>', methods=['POST'])
def update(index):
  name = request.form.get('name')
  contacts[index]['name'] = name
  email = request.form.get('email')
  contacts[index]['email'] = email
  phone = request.form.get('phone')
  contacts[index]['phone'] = phone
  return redirect('/')

# IMPORTANTE V
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)