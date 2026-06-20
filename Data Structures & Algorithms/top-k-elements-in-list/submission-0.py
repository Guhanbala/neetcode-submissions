class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        ans = []

        for _ in range(k):
            max_key = max(freq, key=freq.get)
            ans.append(max_key)
            del freq[max_key]

        return ans