// LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
// https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/

class Solution {
    fun maxPotholes(road: String, budget: Int): Int {
        road = road + "."
        var n = road.length
        var cnt = IntArray(n)
        var k = 0
        var ans = 0
        for (i in 0 until n) {
            var c = road[i]
            if (c == 'x') k++
            else if (k > 0) { cnt[k]++; k = 0; }
        }
        for (k = n - 1; k > 0 && budget > 0; k--) {
            var t = minOf(budget / (k + 1), cnt[k])
            ans += t * k
            budget -= t * (k + 1)
            cnt[k - 1] += cnt[k] - t
        }
        return ans
    }
}
