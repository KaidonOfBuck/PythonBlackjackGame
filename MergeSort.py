# Merge and MergeSort functions

# Merge Sort Function definition
def MergeSort(arr, start, end):
    # Check the start value is lower than the end value
    # and calcualte the mid point of the array
    if start < end:
        mid = start + (end - start) // 2

        MergeSort(arr, start, mid) # Merge sort the first half of the array given
        MergeSort(arr, mid + 1, end) # Merge sort the second half of the array given
        Merge(arr, start, mid, end) # Merge the two sub-arrays into one

# Merge Function definition
def Merge(arr, start, mid, end):
    # Defining the lengths of the sub-arrays
    n1 = mid - start + 1
    n2 = end - mid

    # Defining the sub-arrays with the lengths
    LeftArray = [0] * n1
    RightArray = [0] * n2

    # Filling sub-arrays with values from the original array
    for i in range(0, n1):
        LeftArray[i] = arr[start + i]

    for j in range(0, n2):
        RightArray[j] = arr[mid + 1 + j]

    # Initializing variables for the loops
    i = 0
    j = 0
    k = start # Setting k to the index of the original array

    # While both sub-arrays still have values left
    # check the values of each sub-array against each other
    # and increment the counter for the array whose value is
    # less after adding it to the start of the original array
    # increment the counter for the original array every time
    # the while loop is run.
    while i < n1 and j < n2:
        if LeftArray[i] <= RightArray[j]:
            arr[k] = LeftArray[i]
            i += 1
        else:
            arr[k] = RightArray[j]
            j += 1
        k += 1
    
    # If the sub-arrays are not equal length, add the remaining
    # values from the larger array to the end of the original array
    while i < n1:
        arr[k] = LeftArray[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = RightArray[j]
        j += 1
        k += 1

def MergeSortDeck(arr, start, end):
    # Check the start value is lower than the end value
    # and calcualte the mid point of the array
    if start < end:
        mid = start + (end - start) // 2

        MergeSortDeck(arr, start, mid) # Merge sort the first half of the array given
        MergeSortDeck(arr, mid + 1, end) # Merge sort the second half of the array given
        MergeDecks(arr, start, mid, end) # Merge the two sub-arrays into one

# Unique function to MergeSort a Deck Object (list of Card Objects)
def MergeDecks(arr, start, mid, end):
    # Defining the lengths of the sub-arrays
    n1 = mid - start + 1
    n2 = end - mid

    # Defining the sub-arrays with the lengths
    LeftArray = [0] * n1
    RightArray = [0] * n2

    # Filling sub-arrays with values from the original array
    for i in range(0, n1):
        LeftArray[i] = arr[start + i]

    for j in range(0, n2):
        RightArray[j] = arr[mid + 1 + j]

    # Initializing variables for the loops
    i = 0
    j = 0
    k = start # Setting k to the index of the original array

    # While both sub-arrays still have values left
    # check the values of each sub-array against each other
    # and increment the counter for the array whose value is
    # less after adding it to the start of the original array.
    
    # Increment the counter for the original array every time
    # the while loop is run.
    while i < n1 and j < n2:
        if LeftArray[i].getValue() <= RightArray[j].getValue():
            arr[k] = LeftArray[i]
            i += 1
        else:
            arr[k] = RightArray[j]
            j += 1
        k += 1
    
    # If the sub-arrays are not equal length, add the remaining
    # values from the larger array to the end of the original array
    while i < n1:
        arr[k] = LeftArray[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = RightArray[j]
        j += 1
        k += 1