// LeetCode 3179 - Find the N-th Value After K Seconds
// https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

class Solution {
    fun valueAfterKSeconds(n: Int, k: Int): Int {
        val mod = 1000000007
        var a = IntArray(n)
        for (i in 0 until n) { a[i] = 1 }
        while (k-- > 0) {
            for (i in 1 until n) { a[i] = (a[i] + a[i - 1]) % mod }
        }
        return a[n - 1]
    }
}
