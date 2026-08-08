import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        for right in range(len(nums)):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if q[0] < right - k + 1:
                q.popleft()
            if (right + 1) >= k:
                max_index = q[0]
                res.append(nums[max_index])
        return res
