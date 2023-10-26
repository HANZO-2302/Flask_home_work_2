from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']

		# Создание cookie-файла с данными пользователя
		response = make_response(redirect('/welcome'))
		response.set_cookie('name', name)
		response.set_cookie('email', email)
		return response

	return render_template('index.html')


@app.route('/welcome')
def welcome():
	# Получение данных пользователя из cookie-файла
	name = request.cookies.get('name')

	if name:
		return render_template('welcome.html', name=name)
	else:
		return redirect('/')


@app.route('/logout')
def logout():
	# Удаление cookie-файла
	response = make_response(redirect('/'))
	response.set_cookie('name', '', expires=0)
	response.set_cookie('email', '', expires=0)
	return response


if __name__ == '__main__':
	app.run(debug=True)
