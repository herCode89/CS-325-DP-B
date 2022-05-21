def powersetHelper(Set, user, input, result):
    if Set == len(input):
        hold = []
        for i in user:
            hold.append(i)
        result.append(hold)
        return

    user.append(input[Set])
    powersetHelper(Set + 1, user, input, result)
    user.pop()
    powersetHelper(Set + 1, user, input, result)


def powerset(inputSet):
    result = []
    powersetHelper(0, [], inputSet, result)
    return result


array = [1, 2, 3]
print('Output : ' + str(powerset(array)))
print('The time complexity = O(n!) ')

'''
Author: DURepo
URL: https://github.com/DURepo/CS_325_Exercises/blob/main/Backtracking-permutations.py
Code: 
def permutations(result, str):
    #base Case, print the result when we obtain the result using all characters
    if(len(result) == len(str)):
        print(''.join(result))

    for i in range(len(str)):
        current_choice = str[i]
        # If the choice was not already made we chose it to include in our result
        if(current_choice not in result):
            result.append(current_choice)
            #recursively calling permutations function until we obtain our result
            permutations(result, str)
            #Once we have exhausted all possible paths we backtrack
            result.pop()

def permuations_backtracking(str):
    permutations([],str)

permuations_backtracking("ABC")
----------------------------------------------------------
Author: Permutations Problem in Exploration
Code:
def powerset_helper(pointer, choices_made,input, result):
    if (pointer < 0)):
        append choices_made to results # make a deep copy since we are working with objects
        return

    append input[pointer] to choices_made
    powerset_helper(pointer-1, choices_made, input, result)
    #backtracking
    remove last element added to choices_made
    powerset_helper(pointer - 1, choices_made, input, result)


def powerset(input):
    result = []
    powerset_helper(len(input)-1, [], input, result)
    return result
------------------------------------------------------------
Author: Permutations Problem in Exploration
Code:
if(current_choice not in result):
   result.append(current_choice)
   permutations(result, str)
-----------------------------------------------------------
Author: Group Work
pseudocode explanation:
Main Function:
Initialize empty output array
Call backtracking helper function with the following inputs:
Output array
Input array
Current subset 
Current index
Return output array
Backtracking helper function:
Append a deep copy of the current subset to our output array
Loop from our current (input) index to the length(input array) -1 
Each iteration:
Append the current element to our current subset array
Make recursive call to backtracking helper function with the following
The output array
The original input array
The modified subset
And the current index in the loop +1
Once we finish our recursive stack we pop off the element we added and continue our loop 

'''