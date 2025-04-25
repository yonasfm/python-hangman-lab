# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };

name = input("What is your name? ")
print("Hello, " + name + "!")   


# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";

#   let reverse = "";

#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };

#   alert(reverse);
# };

def reverse_it():
  string = "a man, a plan, a canal, frenemies!"
  reverse = ""
  for i in range(len(string)):
    reverse += string[len(string) - (i + 1)]
  print(reverse)

reverse_it()


# const swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;

#   temp = b;
#   b = a;
#   a = temp;

#   alert("a is now " + a + ", and b is now " + b);
# };

def swap_em():
  a = 10
  b = 30
  temp = None  

  temp = b
  b = a
  a = temp

  print(f"a is now {a}, and b is now {b}") 

# const multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };

#   let total = 1;
#   // let total = ary[0];

#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };

#   return total;
# };

def multiply_array(ary):
  if len(ary) == 0:
    return 1

  total = 1
  # total = ary[0] # This would cause an error if the array is empty

  for i in range(len(ary)):
    total = total * ary[i]

  return total

# Example usage (not part of the original JavaScript, but good for testing)
swap_em()
numbers = [1, 2, 3, 4, 5]
product = multiply_array(numbers)
print(f"The product of the array is: {product}")

empty_array_product = multiply_array([])
print(f"The product of an empty array is: {empty_array_product}")



# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }

def fizzbuzzer(x):
  if x % (3 * 5) == 0:
    return 'fizzbuzz'
  elif x % 3 == 0:
    return 'fizz'
  elif x % 5 == 0:
    return 'buzz'
  else:
    return 'archer'
  

# const nthFibonacciNumber = () => {
#   let fibs = [1, 1];
#   let num = prompt("which fibonacci number do you want?");

#   while (fibs.length < parseInt(num)) {
#     let length = fibs.length;
#     let nextFib = fibs[length - 2] + fibs[length - 1];
#     fibs.push(nextFib);
#   }

#   alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
# };



# const searchArray = (array, value) => {
#   for(let i = 0; i < array.length-1; i++) {
#     if(array[i] == value) {
#       return true;
#       break;
#     }
#   }
#   return -1;
# };

def search_array(array, value):
  for i in range(len(array)):
    if array[i] == value:
      return True
      break  # Although 'break' is redundant after 'return', it's kept for direct translation
  return -1


my_array = [5, 10, 15, 20, 25]
search_value = 15
result = search_array(my_array, search_value)
print(f"Is {search_value} in the array? {result}")

search_value = 30
result = search_array(my_array, search_value)
print(f"Is {search_value} in the array? {result}")

# const isPalindrome = (str) => {
#   for(let i = 0; i < str.length/2; i++){
#     if(str[i] != str[str.length-i-1]){
#       return false;
#       break;
#     }
#   }
#   return true;
# };

def is_palindrome(str):
  for i in range(len(str) // 2):
    if str[i] != str[len(str) - 1 - i]:
      return False
      break  # Although 'break' is redundant after 'return', it's kept for direct translation
  return True


print(is_palindrome("racecar"))   # Output: True
print(is_palindrome("hello"))     # Output: False
print(is_palindrome("madam"))     # Output: True
print(is_palindrome(""))        # Output: True (an empty string is often considered a palindrome)
print(is_palindrome("a"))       # Output: True (a single character is a palindrome)


# const hasDupes = (arr) => {
#   let obj = {};
#   for (i = 0; i < arr.length; i++) {
#     if(obj[arr[i]]) {
#       return true;
#     }
#     else {
#       obj[arr[i]] = true;
#     }
#   }
#   return false;
# };

def has_dupes(arr):
  obj = {}
  for i in range(len(arr)):
    if arr[i] in obj:
      return True
    else:
      obj[arr[i]] = True
  return False


array1 = [1, 2, 3, 4, 5]
print(f"Does {array1} have duplicates? {has_dupes(array1)}")  # Output: False

array2 = [1, 2, 3, 2, 5]
print(f"Does {array2} have duplicates? {has_dupes(array2)}")  # Output: True

array3 = []
print(f"Does {array3} have duplicates? {has_dupes(array3)}")  # Output: False