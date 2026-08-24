// LeetCode 3582 - Generate Tag for Video Caption
// https://leetcode.com/problems/generate-tag-for-video-caption/

class Solution {
    fun generateTag(caption: String): String {
        var ans = StringBuilder("#")
        var words = caption.trim().split("\\s+")
        var i = 0
        for (word in words) {
            if (word.isEmpty()) continue
            var w = StringBuilder(word.toLowerCase())
            if (i == 0) ans.append(w)
            else {
                if (w.length > 0) w.setCharAt(0, w[0].uppercaseChar())
                ans.append(w)
            }
            if (ans.length >= 100) break
            i = i + 1
        }
        if (ans.length > 100) ans.setLength(100)
        return ans.toString()
    }
}
