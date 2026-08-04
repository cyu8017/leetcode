// LeetCode 1151 - Minimum Swaps to Group All 1's Together
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

class Solution {
    fun minSwaps(data: IntArray): Int {
        val ones = data.sum()
        if (ones <= 1) return 0
        var cur = data.take(ones).sum()
        var best = cur
        for (i in ones until data.size) {
            cur += data[i] - data[i - ones]
            best = maxOf(best, cur)
        }
        return ones - best
    }
}
