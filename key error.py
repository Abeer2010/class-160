dictionary = {"fruit":"mango","colour":"pink","bird":"sparrow"}
try:
    print(dictionary["animal"])
except(KeyError):
    print("Key Animal is not present in dictionary")