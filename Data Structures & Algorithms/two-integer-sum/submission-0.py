class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen_numbers:
                return [seen_numbers[complement], index]
            seen_numbers[num] = index

