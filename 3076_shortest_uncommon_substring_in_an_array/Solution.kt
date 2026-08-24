// LeetCode 3076 - Shortest Uncommon Substring in an Array
// https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

class Solution {
    fun shortestSubstrings(arr: Array<String>): Array<String> {
        var n = arr.size
        var ans = arrayOfNulls<String>(n)
        for (i in 0 until n) { ans[i] = "" }
        for (i in 0 until n) {
            var s = arr[i]
            var m = s.length
            for (j in 1 until = m && ans[i].isEmpty()) {
                for (l in 0 until = m - j) {
                    var sub = s.substring(l, l + j)
                    if (ans[i].isEmpty() || ans[i].compareTo(sub) > 0) {
                        var ok = true
                        for (k in 0 until n) {
                            if (k != i && arr[k].contains(sub)) {
                                ok = false
                                break
                            }
                        }
                        if (ok) ans[i] = sub
                    }
                }
            }
        }
        return ans
    }
}
