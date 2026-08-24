// LeetCode 2607 - Make K-Subarray Sums Equal
// https://leetcode.com/problems/make-k-subarray-sums-equal/

class Solution {
    fun makeSubKSumEqual(arr: IntArray, k: Int): Long {
        var n = arr.size
        var g = gcd(n, k)
        var ans = 0
        for (r in 0 until g) {
            var group = ArrayList<Int>()
            run {
                var i = r
                while (i < n) {
                    group.add(arr[i])
                    i += g
                }
            }
            group.sort()
            var med = group[group.size / 2]
            for (x in group) { ans += kotlin.math.abs(x - med) }
        }
        return ans
    }

    private fun gcd(a: Int, b: Int): Int {
        while (b != 0) {
            var t = a % b
            a = b
            b = t
        }
        return a
    }
}
