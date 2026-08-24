// LeetCode 3722 - Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

class Solution {
    fun lexSmallest(s: String): String {
        var ans = s
        var n = s.length
        for (k in 1 ..n) {
            var a1 = s.toCharArray()
            reverse(a1, 0, 0 + k)
            var t1 = String(a1)
            var a2 = s.toCharArray()
            reverse(a2, n - k, n - k + k)
            var t2 = String(a2)
            if (t1.compareTo(ans) < 0) ans = t1
            if (t2.compareTo(ans) < 0) ans = t2
        }
        return ans
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
