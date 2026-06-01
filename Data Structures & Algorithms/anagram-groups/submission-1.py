class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagram_map = defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))
            anagram_map[key].append(i)
        return list(anagram_map.values())
