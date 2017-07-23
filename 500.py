class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = {
            'qwertyuiop',
            'asdfghjkl',
            'zxcvbnm'
        }
        rows = {row + row.upper() for row in rows}
        result = []
        for word in words:
            if any(all(letter in row for letter in word)
                    for row in rows):
                result.append(word)
        return result


if __name__ == '__main__':
    print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))
        
