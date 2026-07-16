# LeetCode 0948 - Bag of Tokens
# https://leetcode.com/problems/bag-of-tokens/

class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        i, j = 0, len(tokens) - 1
        score = ans = 0
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                i += 1
                score += 1
                ans = max(ans, score)
            elif score:
                power += tokens[j]
                j -= 1
                score -= 1
            else:
                break
        return ans
