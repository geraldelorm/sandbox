from module import connect

#good to have a main functions
def main() -> None:
    connect()


# Use type hints
number: int = "abc" #type flag for wrong usage of number variable

def upper_everything(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]

sample: list[int] = ["a", 1, 2, 3, "yes"] #pycharm cannot check this properly - install mypy

#list comprehensions
people: list[str] = ["James", "Charlotte", "Stephany", "Mario", "Sandra"]

long_names = [person for person in people if len(person) > 7 ]
print(F"Long Names: {long_names}")





'''
main() and if __name__ == "main" can be done quickly in pycharm with live templates - by typing "main" -> Press Enter key
'''
# call main function in main
if __name__ == "__main__":
    main()




