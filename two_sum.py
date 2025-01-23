class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0, len(nums)):
            cur = nums[i]
            x = target - cur
            if x in map.keys():
                return map[x], i
            map[cur] = i