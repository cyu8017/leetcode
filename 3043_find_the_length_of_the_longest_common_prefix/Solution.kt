// LeetCode 3043 - Find the Length of the Longest Common Prefix
// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

class Solution {
    fun longestCommonPrefix(arr1: IntArray, arr2: IntArray): Int {
        var s = HashSet<Int>()
        for (x0 in arr1) {
            run {
                var x = x0
                while (x > 0) {
                    s.add(x)
                    x /= 10
                }
            }
        }
        var mx = 0
        for (x0 in arr2) {
            var x = x0
            while (x > 0) {
                if (s.contains(x)) {
                    mx = maxOf(mx, x)
                    break
                }
                x /= 10
            }
        }
        return if (mx > 0) mx.toString().length else 0
    }
}
