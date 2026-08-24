// LeetCode 3583 - Count Special Triplets
// https://leetcode.com/problems/count-special-triplets/

class Solution {
    fun specialTriplets(nums: IntArray): Int {
        var left = HashMap<Int, Int>()
        var right = HashMap<Int, Int>()
        for (x in nums) {
            if (!right.containsKey(x)) right[x] = 0
            right[x] = right[x] + 1
        }
        var ans = 0
        var mod = 1000000007
        for (x in nums) {
            right[x] = right[x] - 1
            var lv = if (left.containsKey(x * 2)) left[x * 2] else 0
            var rv = if (right.containsKey(x * 2)) right[x * 2] else 0
            ans = (ans + lv * rv % mod) % mod
            if (!left.containsKey(x)) left[x] = 0
            left[x] = left[x] + 1
        }
        return ans
    }
}
