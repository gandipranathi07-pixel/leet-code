class Solution(object):
    def twoSum(self, numbers, target):

        L = 0
        R = len(numbers) - 1

        while L < R:

            current_sum = numbers[L] + numbers[R]

            if current_sum == target:
                return [L + 1, R + 1]

            elif current_sum < target:
                L += 1

            else:
                R -= 1
        