from colorama import Fore

# Returns 1 if element found, -1 if not found!
def binarySearch(numbers: list, low, high, element: int):
    # Check if high is greater than low (0 in most of the cases!)
    if high >= low:

        mid = low + (high - low) // 2

        # If element found at mid!
        if int(numbers[mid]) == element:
            visualize(numbers, mid, element, flag=1) # Calling visualize() with fage value as 1 --> Flag value 1 reprs that element is found at mid position and mark mid as green!
            return mid

        # If element is smaller than number[mid] search in right sub array!
        elif int(numbers[mid]) > element:
            visualize(numbers, mid, element)
            return binarySearch(numbers, low, mid - 1,
                                element)  # Calling function recursivily with new parameters (low=low, high=mid-1[only till left sub array!])

        # If element is larger than number[mid] Searching in right sub array!
        else:
            visualize(numbers, mid, element)
            return binarySearch(numbers, mid + 1, high, element)

    else:
        # Element is not present in the array
        visualize(numbers, mid=0, element=0, flag=2)  # Calling visualize() with flag 2, Flag value 2 reprs that the element is not present inside the list of numbers hence mark all the numbers as red.
        return -1

notToBeChecked = []
numberOfPass = 0 

def visualize(numbers: list, mid, element, flag=0):
    global notToBeChecked
    global numberOfPass

    """
    Red will be the elements which does not need to be checked.
    Green will be the element itself.
    Low is the staring point of the list.
    High is the end of the list.
    yellow will be the mid element for the current pass
    """

    nextPass = f"""
    ####################################################
        Pass: {numberOfPass}             
    ####################################################
    """


    print(Fore.CYAN, nextPass) 
    numberOfPass += 1 

    toCheck = ''
    notToCheck = ''
    low  = 0
    high = len(numbers)

    if flag == 1:      # Element found at mid!
        for i in range(0, mid):
            notToCheck += f'({numbers[i]},i={i}), '
        found = f'({numbers[mid]},i={mid}), '
        notToCheck2 = ''
        for i in range(mid+1, high):
            notToCheck2 += f'({numbers[i]},i={i}), '
        print(Fore.RED, notToCheck, end='')     # Marking 1st half of list as red.
        print(Fore.GREEN, found, end='')        # Marking mid value as green.
        print(Fore.RED, notToCheck2, end='')    # Marking 2nd half of the list as red.
        return 

    if flag == 2:           # Element not found inside the list
        for i in range(low, high):
            notToCheck += f'({numbers[i]},i={i}), '
        print(Fore.RED, notToCheck)                 # Marking full list as red.
        return 

    if element > int(numbers[mid]):     # Element present in right sub array.

        for i in range(mid + 1, high):
            if numbers[i] not in notToBeChecked:        # Check if the element is already appended to notToBeChecked list.
                toCheck += f'({numbers[i]},i={i}), '
           
        for i in range(low, mid):
            notToCheck += f'({numbers[i]},i={i}), '
            notToBeChecked.append(numbers[i])             # Appending element to notToBeChecked List.

        # Printing according to the toCheck and notToCheck
        print(Fore.RED, notToCheck, end="")
        print(Fore.YELLOW, f'({numbers[mid]},i={mid}), ', end="")
        print(Fore.RESET, toCheck, end="")
        return 

    elif element < int(numbers[mid]):   

        for i in range(mid + 1, high):
            notToCheck += f'({numbers[i]},i={i}), '
            notToBeChecked.append(numbers[i])
        for i in range(low, mid ):
            if numbers[i] not in notToBeChecked:
                toCheck += f'({numbers[i]},i={i}), '

        # Printing according to the toCheck and notToCheck
        print(Fore.RESET, toCheck, end="")
        print(Fore.YELLOW, f'({numbers[mid]},i={mid}), ', end="")
        print(Fore.RED, notToCheck, end="")
        return 

# main() [driver code]

numbers = input("Enter the list of elements: ")  # List of elements.

if ',' in numbers:      # for ',' sep list 
    numbers = numbers.split(',')

elif ' ' in numbers:       # for ' ' sep list
    numbers = numbers.split(' ')

else:           # If list has only one number!
    try:
        numbers = int(numbers)
    except:
        print("Enter a valid list of numeric elements!")

element = int(input("Enter the element to be searched: "))  # Element to be searched!

low = 0 # Search starts from the first element of the list.
high = len(numbers) # To the end of the list.
result = binarySearch(numbers, low, high, element)  # Getting result into result variable

if result == 1:     # Checking if found or not.
    print("[*]Element Found!!")
else:
    print("[*]Element not found!!")