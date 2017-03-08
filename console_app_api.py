import requests #imports the request module

print "Hello, register to get subscribed to or github events channel "
github_name = input('Enter your github name: ')
response  = requests.get('https://api.github.com/events'.format(github_name))

print response.json()
