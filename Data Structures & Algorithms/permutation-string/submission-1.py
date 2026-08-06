class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        if len(s1) > len(s2):
            return False
        
        s1_count = {}
        window_count = {}

        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        for right in range(len(s2)):
            char_right = s2[right]
            window_count[char_right] = 1 + window_count.get(char_right, 0)
            if (right - left + 1) > len(s1):
                char_left = s2[left]
                window_count[char_left] -= 1

                if window_count[char_left] == 0:
                    del window_count[char_left]
                left += 1
            if window_count == s1_count:
                return True
        return False


        