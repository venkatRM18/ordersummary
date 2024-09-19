import re

sum = 0

pattern = 'py'

if re.match(pattern, 'python.txt'):
  sum +=1
if re.match(pattern, 'text.py'):
  sum += 2
if re.match(pattern, 'herepyfile'):
  sum += 4
if re.match(pattern, 'numpy'):
  sum += 8
print(sum)