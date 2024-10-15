class Solution1:
    def majority_element(self, nums):
        n = len(nums)
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > n / 2:
                return num
            

# Best Solution
class Solution2:
    def majority_element(self, nums):
        candidate = 0
        votes = 0
        for num in nums:
            if votes == 0:
                candidate = num
            votes += (1 if candidate == num else -1)
        return candidate


class Solution3:
    def majority_element(self, nums):
        nums.sort()
        return nums[len(nums) // 2]
