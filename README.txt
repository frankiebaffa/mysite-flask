These are the source files for my website hosted on pythonanywhere.com.  It is built to be a portfolio site for all of the projects that I am currently working on, software and other.  The design of the website is built for a single user login who would function as the admin for the page, capable of adding content through the CRUD pages.

To install:

	git clone https://github.com/frankiebaffa/my-site

	cd mysite-flask

	[ create a python virtual environment.  I use virtualenv so I use: ]
	virtualenv --python=/path/to/your/python3.6/interpreter yourvirtualenvname

	source yourvirtualenvname/bin/activate

	pip3.6 install -r requirements.txt

	cd mysite

	[on Mac/Linux]
	export FLASK_APP=frankiebaffa.py

	[on Windows CMD]
	set FLASK_APP=frankiebaffa.py

 	[on Windows PowerShell]
	$env:FLASK_APP = "frankiebaffa.py"

	sudo flask db upgrade

	sudo flask run
