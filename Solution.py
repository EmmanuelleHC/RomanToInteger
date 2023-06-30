class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        values = list(map(lambda c: dict_roman[c], s[::-1]))  # Convert Roman numerals to corresponding values
        total = 0
        prev_value = 0

        for value in values:
            if value >= prev_value:
                total += value
            else:
                total -= value
            prev_value = value

        return total
