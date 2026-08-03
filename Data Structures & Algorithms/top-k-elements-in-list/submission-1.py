class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            freqMap[num] = 1 + freqMap.get(num,0)
        
        freqList = []

        for key in freqMap.keys():
            freqList.append([freqMap[key], key])
        
        freqList.sort()

        results = []

        while True:
            results.append(freqList.pop()[1])
            if len(results) == k:
                break
        
        return results

