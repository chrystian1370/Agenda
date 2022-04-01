from flask import Flask, render_template, request, redirect
app = Flask('app')

todos = [
  { 
    'title': 'Chrystian Alvarenga',
    'category':'chrystianalvarenga@hotmail.com',
    'telephone':'(16)99460-3667'    
  }
]

@app.route('/')
def index():
  return render_template('index.html',todos=todos)

@app.route('/create', methods=['POST'])
def create():
  title = request.form.get('title')
  cat = request.form.get('category')
  tel = request.form.get('telephone')
  todos.append({
    'title': title,   
    'category': cat,
    'telephone': tel,
  })
  return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
  todos.pop(index)
  return redirect('/')


@app.route('/update/<int:index>', methods=['POST'])
def update(index):
  title = request.form.get('title')
  todos[index]['title'] = title
  category = request.form.get('category')
  todos[index]['category'] = category
  telephone = request.form.get('telephone')
  todos[index]['telephone'] = telephone
  return redirect('/')

# IMPORTANTE V
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)