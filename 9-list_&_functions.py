days = ["sin","two","carter","kionjo","friday"]
numbers = [1, 2, 35, 6, 3, 2, 3, 433, 32, 3, 32, 43, 555, 4, 4, 66, 64]
days.extend(numbers)
numbers.sort()
numbers.reverse()
print(days)
numbers.append("handsome")
print(numbers)
days.insert(1, "samson")
print(days)
days.remove("carter")
print(days)
days.pop()
print(days)
print(days.index("kionjo"))
print(numbers.count(2))
weeks = days.copy()
print(weeks)





