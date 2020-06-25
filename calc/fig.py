from cgi import parse_qs
from template import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a',[''])[0] 
	b = d.get('b',[''])[0]

	if a == '' and b == '':
		sum = 'None'
		mul = 'None'

	elif a.isdigit() and b.isdigit():
		a, b = int(a), int(b)
		sum = a+b
		mul = a*b
	else:
		sum = '?'
		mul = '?'
	response_body = html % {
		'sum':sum,
		'mul':mul,
	}

	status = '200 OK'
	response_headers = [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	]
	
	start_response(status, response_headers)
	return [response_body]
