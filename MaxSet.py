def max_independent_set(nums):
    dynamic = [0] * len(nums)
    dynamic[0] = nums[0]
    if len(nums) >= 2:
        dynamic[1] = max(dynamic[0], nums[1])
    results = max(dynamic[0], dynamic[1])
    for i in range(2, len(nums)):
        dynamic[i] = max(dynamic[i - 1],
                         dynamic[i - 2],
                         dynamic[i - 2] + nums[i],
                         nums[i])
        results = max(results, dynamic[i])
    return results


nums1 = [7, 2, 5, 8, 6]
print('Maximum possible sum: ' + str(max_independent_set(nums1)))

nums2 = [-1, -1, 0]
print('Maximum possible sum: ' + str(max_independent_set(nums2)))

nums3 = [-1, -1, -10, -34]
print('Maximum possible sum: ' + str(max_independent_set(nums3)))

print('The time complexity = O(n) ')

'''
Author: coecs325
URL:https://replit.com/@coecs325/unboundknapsack
Code:

def unbound_knapsack(W, n, weights, values):
    dp = [0]*(W+1)

    for x in range(1, W+1):

        for i in range(n):
            wi = weights[i]
            if wi <= x:
                dp[x] = max(dp[x] , dp[x-wi] + values[i])

    return dp[W]


print(unbound_knapsack(10,5,[4,9,3,5,7], [10,25,13,20,8]))

------------------------------------------------------------------
Author: Exploration: Dynamic Programming - Unbound Knapsack Problem
URL: Module 4
Code:
unbound_knapsack(W, n, weights[], values[]):
  dp = [0]*(W+1) #initalize base case and other subproblem values to 0
  for x in range(W+1):
    for i in range(n):
      if wi <= x:
          dp[x] = max(dp[x] , dp[x-wi] + vi)
  return dp[W]
-------------------------------------------------------------------
Concept Understanding: https://en.wikipedia.org/wiki/Knapsack_problem#Applications

---------------------------------------------------------------------


'''
