// LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
// https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

class Solution {
    fun minimumOperations(nums: IntArray): Int {
        var list = ArrayList<Int>()
        for (x in nums) { list.add(x) }
        var ops = 0
        while (true) {
            var seen = HashSet<Int>()
            var dup = false
            for (x in list) {
                if (!seen.add(x)) { dup = true; break; }
            }
            if (!dup) return ops
            if (list.size <= 3) return ops + 1
            list.subList(0, 3).clear()
            ops = ops + 1
        }
    }
}
