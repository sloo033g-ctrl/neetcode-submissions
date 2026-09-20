from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map sorted string keys to lists of original strings
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sorting a string returns a list of characters, tuple makes it hashable
            key = tuple(sorted(s))
            anagram_map[key].append(s)
            
        return list(anagram_map.values())
