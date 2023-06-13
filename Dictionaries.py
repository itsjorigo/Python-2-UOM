my_first_dict = dict()

scores = {'Saman': 75, 'Nimal': 80, 'Kamal' : 65}

print(scores['Saman'])
print(scores.get('Nimal'))

scores['Sunil'] = 60
print(scores)

scores['Saman'] = 70
print(scores)

# scores.pop('Nimal')
# print(scores)
#
# scores.clear()
# print(scores)

all_keys = list(scores.keys())
print(all_keys)

all_values = list(scores.values())
print(all_values)


for key in scores:
    print(key, scores[key])