class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        incr1 = m - 1
        incr2 = n - 1
        for i in range(0, n+m):
            if (incr2 < n and nums2[incr2] <= nums1[incr1]):
                nums1.insert(incr1, nums2[incr2])
                incr2 += 1
            else:
                incr1 += 1