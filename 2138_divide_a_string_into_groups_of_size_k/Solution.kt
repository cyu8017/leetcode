// LeetCode 2138 - Divide a String Into Groups of Size k
// https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

class Solution {
    fun divideString(s: String, k: Int, fill: Char): Array<String> {
        var ans = mutableListOf()
        var i = 0
        while (i < s.length) {
            if (i + k <= s.length) ans.add(s.substring(i, i + k))
            else {
                StringBuilder chunk = StringBuilder(s.substring(i))
                while (chunk.length < k) chunk.append(fill)
                ans.add(chunk.toString())
                i += k
            }
        }
        return ans.toArray(arrayOfNulls<String>(0))
    }
}
