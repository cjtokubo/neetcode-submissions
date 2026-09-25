class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums = sorted(enumerate(nums), key=lambda x: x[1])

        mysum = None
        left = 0
        right = len(nums) - 1

        while (mysum != target):

            mysum = nums[left][1] + nums[right][1]

            if (mysum < target):
                left += 1
            elif (mysum > target):
                right -= 1
            else:
                return sorted([nums[left][0],nums[right][0]])