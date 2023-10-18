states = {'MS':'Mississippi',
          'VA':'Virginia',
          'AL':'Alabama',
          "TN":'Tennessee'}
for key in states:
    print(key, states[key], sep = ',')
print(len(states))
x=states.get("TN")
print(x)
y= states.get('PA','Pennsylvania')
print(y)

states_capital_city = [
    {"state_code": "MS","capital": "Jackson"},
    {"state_code": "VA","capital": "Rich"},
    {"state_code": "AL","capital": "Mongomery"},
    {"state_code": "TN","capital": "Nashiville"},
]

print()
for ele in states_capital_city:
    print(ele["state_code"],ele["capital"],sep=', ')