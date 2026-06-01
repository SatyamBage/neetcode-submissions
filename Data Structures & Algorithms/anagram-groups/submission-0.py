class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagram_map = defaultdict(list)
        for i in strs:
            sorted_key = "".join(sorted(i))
            anagram_map[sorted_key].append(i)
        return list(anagram_map.values())
