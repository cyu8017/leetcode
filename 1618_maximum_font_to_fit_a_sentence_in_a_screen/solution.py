class FontInfo:
    def getWidth(self, fontSize, ch): return fontSize
    def getHeight(self, fontSize): return fontSize
class Solution:
    def maxFont(self, text, w, h, fonts, fontInfo=None):
        fontInfo = fontInfo or FontInfo()
        lo, hi, ans = 0, len(fonts) - 1, -1
        while lo <= hi:
            mid = (lo + hi) // 2; f = fonts[mid]
            fits = fontInfo.getHeight(f) <= h and sum(fontInfo.getWidth(f, c) for c in text) <= w
            if fits: ans = f; lo = mid + 1
            else: hi = mid - 1
        return ans
