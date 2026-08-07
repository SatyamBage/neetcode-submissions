class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        count_t = {}
        window = {}

        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)

        have = 0
        need = len(count_t)

        res = [-1, -1]
        res_len = float("infinity")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)
            if char in count_t and window[char] == count_t[char]:
                have += 1
            while have == need:
                current_window_size = right - left + 1
                if current_window_size < res_len:
                    res = [left, right]
                    res_len = current_window_size
                left_char = s[left]
                window[left_char] -= 1
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                left += 1
        left_index, right_index = res
        return s[left_index : right_index + 1] if res_len != float("infinity") else ""

