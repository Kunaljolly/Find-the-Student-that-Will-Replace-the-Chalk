class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if len(chalk) == 1:
            return 0
        i = 0
        s = sum(chalk)
        while(k>= s):
            k -= s
        if s < k :
            while(k>= chalk[i]):
                if i == len(chalk)-1:
                    i = -1
                k -= chalk[i]
                i += 1
        else:
            while(k>= chalk[i]):
                k -= chalk[i]
                i += 1
        return i
