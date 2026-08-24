# LeetCode 3582 - Generate Tag for Video Caption
# https://leetcode.com/problems/generate-tag-for-video-caption/


class Solution:
    def generateTag(self, caption: str) -> str:
        ans = "#"
        words = caption.strip().split()
        i = 0
        for word in words:
            if not word:
                continue
            w = word.lower()
            if i == 0:
                ans += w
            else:
                if w:
                    w = w[0].upper() + w[1:]
                ans += w
            if len(ans) >= 100:
                break
            i += 1
        if len(ans) > 100:
            ans = ans[:100]
        return ans
