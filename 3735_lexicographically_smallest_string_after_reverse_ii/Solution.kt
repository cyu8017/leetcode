// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

class Solution {
    fun lexSmallest(s: String): String {
        var n = s.length
        var best = s
        for (i in 1 ..n) {
            var t = s.toCharArray()
            reverse(t, 0, 0 + i)
            var ts = String(t)
            if (ts.compareTo(best) < 0) best = ts
        }
        for (i in 0 until n) {
            var t = s.toCharArray()
            reverse(t, i, i + n - i)
            var ts = String(t)
            if (ts.compareTo(best) < 0) best = ts
        }
        return best
    }

    private fun reverse(a: CharArray) { reverse(a, 0, a.size) }
    private fun reverse(a: CharArray, l: Int, r: Int) {
        var i = l
        var j = r - 1
        while (i < j) {
            var t = a[i]; a[i] = a[j]; a[j] = t
            i += 1; j -= 1
        }
    }
    private fun reverse(a: IntArray) { reverse(a, 0, a.size) }
    private fun reverse(a: IntArray, l: Int, r: Int) {
        var i = l
        var j = r - 1
        while (i < j) {
            var t = a[i]; a[i] = a[j]; a[j] = t
            i += 1; j -= 1
        }
    }
}
