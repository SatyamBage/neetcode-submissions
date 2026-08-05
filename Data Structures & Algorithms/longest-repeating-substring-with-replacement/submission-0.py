class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            char = s[right]
            count[char] = 1 + count.get(char, 0)
            max_freq = max(count.values())

            while (right - left + 1) - max_freq > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        return max_length
