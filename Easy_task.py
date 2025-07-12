#Check  Number is Odd or Even
def check_odd_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: "))
print("The number is:", check_odd_even(num))
#-------------------------
# Convert Minutes to Hours and Minutes
def convert_minutes(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes
mins = int(input("Enter total minutes: "))
h, m = convert_minutes(mins)
print(f"{h} hours and {m} minutes")
#-------------------------
#Count Words in a Sentence
def count_words(sentence):
    words = sentence.split()
    return len(words)
user_input = input("Enter a sentence: ")
print("Total words:", count_words(user_input))
#--------------------------
#Reverse the Order of Words in a Sentence
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
text = input("Enter a sentence: ")
print("Reversed sentence:", reverse_words(text))
#----------------------------
#Calculate the Square of Each Number in a List
def square_list(numbers):
    squares = []
    for num in numbers:
        squares.append(num ** 2)
    return squares
nums = [1, 2, 3, 4, 5]
print("Squares:", square_list(nums))
#------------------------------