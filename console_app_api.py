import requests #imports the request module

print "Hello, register to get subscribed to github events channel "
github_name = raw_input('Enter your github name: ')
response  = requests.get('https://api.github.com/users/tater/events'.format(github_name))

print response.json()
