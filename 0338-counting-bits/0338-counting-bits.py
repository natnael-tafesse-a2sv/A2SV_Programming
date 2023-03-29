class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n + 1):
            count = 0
            for _ in range(20):
                if num & 1:
                    count += 1
                num = num >> 1
            ans.append(count)
        return ans