class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return sum(
            int(digit)
            for digit in bin(x ^ y)[2:]
        ) 


if __name__ == '__main__':
    test = Solution().hammingDistance(1, 4)
    print(test)
