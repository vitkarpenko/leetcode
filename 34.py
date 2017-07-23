import bisect


class Solution(object):
    @staticmethod
    def index_left(a, x):
	i = bisect.bisect_left(a, x)
	if i != len(a) and a[i] == x:
	    return i
	raise ValueError

    @staticmethod
    def index_right(a, x):
	i = bisect.bisect_right(a, x)
	if a[i-1] == x:
	    return i-1
	raise ValueError

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            left = Solution.index_left(nums, target)
            right = Solution.index_right(nums, target)
        except ValueError:
            return [-1, -1]
        else:
            return [left, right]


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
