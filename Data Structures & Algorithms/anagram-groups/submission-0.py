class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict with sorted anagram as key
        strMap = defaultdict(list)

        for word in strs:
            myKey = ''.join(sorted(word))
            strMap[myKey].append(word)

        return list(strMap.values())