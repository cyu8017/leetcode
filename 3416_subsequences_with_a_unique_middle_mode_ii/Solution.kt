// LeetCode 3416 - Subsequences with a Unique Middle Mode II
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-ii/

class Solution {
    private fun uniqueMode(a: IntArray): Boolean {
        var freq = HashMap<Int, Int>()
        for (x in a) { freq.merge(x, 1, Int::plus) }
        var best = 0
        var cnt = 0
        for (f in freq.values) {
            if (f > best) { best = f; cnt = 1; }
            else if (f == best) cnt++
        }
        cnt = = 1
        return cnt
    }

    fun subsequencesWithMiddleMode(nums: IntArray): Int {
        val mod = 1_000_000_007
        var n = nums.size
        var ans = 0
        for (mid in 2 until n - 2) {
            for (a in 0 until mid) {
                for (b in a + 1 until mid) {
                    for (c in mid + 1 until n) {
                        for (d in c + 1 until n) {
                            var seq = {nums[a], nums[b], nums[mid], nums[c], nums[d]}
                            if (uniqueMode(seq)) ans = (ans + 1) % mod
                        }
                    }
                }
            }
        }
        return ans
    }
}
