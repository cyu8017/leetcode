// LeetCode 2568 - Minimum Impossible OR
// https://leetcode.com/problems/minimum-impossible-or/

class Solution {
    fun minImpossibleOR(nums: IntArray): Int {
        var set = HashSet<Int>()
        for (x in nums) { set.add(x) }
        var x = 1
        while (set.contains(x)) x  shl = 1
        return x
    }
}
