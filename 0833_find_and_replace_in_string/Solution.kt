// LeetCode 0833 - Find And Replace in String
// https://leetcode.com/problems/find-and-replace-in-string/

class Solution {
    fun findReplaceString(s: String, indices: IntArray, sources: Array<String>, targets: Array<String>): String {
        var replaceIdx = HashMap<Int, IntArray>()
        var replaceStr = HashMap<Int, String>()
        for (k in 0 until indices.size) {
            var i = indices[k]
            if (s.startsWith(sources[k], i)) {
                replaceIdx[i] = intArrayOf(sources[k].length)
                replaceStr[i] = targets[k]
            }
        }
        var out = StringBuilder()
        var i = 0, n = s.length
        while (i < n) {
            if (replaceStr.containsKey(i)) {
                out.append(replaceStr[i])
                i += replaceIdx[i][0]
            } else {
                out.append(s[i])
                i++
            }
        }
        return out.toString()
    }
}
