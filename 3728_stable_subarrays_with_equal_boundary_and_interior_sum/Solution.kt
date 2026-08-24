// LeetCode 3728 - Stable Subarrays With Equal Boundary And Interior Sum
// https://leetcode.com/problems/stable_subarrays_with_equal_boundary_and_interior_sum/

class Solution {
    fun countStableSubarrays(capacity: IntArray): Long {
        var n = capacity.size
        var s = LongArray(n + 1)
        for (i in 1 ..n) { s[i] = s[i - 1] + capacity[i - 1] }
        var cnt = HashMap<String, Int>()
        var ans = 0
        for (r in 2 until n) {
            var l = r - 2
            var keyL = capacity[l] + "#" + (capacity[l] + s[l + 1])
            cnt[keyL] = cnt.getOrDefault(keyL, 0) + 1
            var keyR = capacity[r] + "#" + s[r]
            ans += cnt.getOrDefault(keyR, 0)
        }
        return ans
    }
}
