import collections


class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        LHS = 0
        for count in counts:
            if count+1 in counts:
                LHS = max(LHS, counts[count] + counts[count+1])
        return LHS


if __name__ == '__main__':
    print(Solution().findLHS([1,3,2,2,5,2,3,7]))

