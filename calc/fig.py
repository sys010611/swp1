from cgi import parse_qs
from template import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a','0')[0] #a,b = 0 if no input
	b = d.get('b','0')[0]

	a, b = int(a), int(b)

	response_body = html % {
		'sum':[a+b],
		'mul':[a*b],
	}

	status = '200 OK'
	response_headers = [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	]
	
	start_response(status, response_headers)
	return [response_body]
