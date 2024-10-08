# Best Solution
class Solution1:
    def remove_element(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    

class Solution2:
    def remove_element(self, nums, val):
        k = len(nums)
        while val in nums:
            nums.remove(val)
            k -= 1
        return k


class Solution3:
    def remove_element(self, nums, val):
        k = 0
        while k < len(nums):
            if nums[k] == val:
                nums.pop(k)
            else:
                k += 1
        return k