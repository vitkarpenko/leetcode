import itertools


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not(nums):
            return 0
        length = max(len(bin(num)) for num in nums) - 2
        template = '{{:0{}b}}'.format(length)
        return sum(
            b.count('0') * b.count('1')
            for b in itertools.zip_longest(*(template.format(num) for num in nums))
        )



if __name__ == '__main__':
    test = Solution().totalHammingDistance([4, 14, 4])
    print(test)
        	
        
