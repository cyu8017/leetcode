// LeetCode 1618 - Maximum Font to Fit a Sentence in a Screen
// https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/

interface FontInfo {
    fun getWidth(fontSize: Int, ch: Char): Int
    fun getHeight(fontSize: Int): Int
}

class Solution {
    fun maxFont(text: String, w: Int, h: Int, fonts: IntArray, fontInfo: FontInfo): Int {
        var lo = 0
        var hi = fonts.size - 1
        var ans = -1
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            val f = fonts[mid]
            var fits = fontInfo.getHeight(f) <= h
            if (fits) {
                var width = 0L
                for (c in text) width += fontInfo.getWidth(f, c)
                fits = width <= w
            }
            if (fits) {
                ans = f
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return ans
    }

    fun maxFont(text: String, w: Int, h: Int, fonts: IntArray): Int {
        return maxFont(text, w, h, fonts, object : FontInfo {
            override fun getWidth(fontSize: Int, ch: Char) = fontSize
            override fun getHeight(fontSize: Int) = fontSize
        })
    }
}
