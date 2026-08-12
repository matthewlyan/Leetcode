class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        most frequent element, we want to get
        if we use a max heap we can pop off the most common one

        get the count of the numbers in some dictionary
        
        after that initalize the max heap where it looks like (-freq,num) 

        we iterate while k and then we pop off the most frequent count into a new array
        """

        count = Counter(nums)

        maxHeap = [(-freq,num) for num,freq in count.items()]

        res = []
        heapq.heapify(maxHeap)
        while k:
            freq,num = heapq.heappop(maxHeap)
            res.append(num)
            k -= 1
        return res