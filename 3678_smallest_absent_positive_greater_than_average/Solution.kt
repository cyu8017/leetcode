// LeetCode 3678 - Smallest Absent Positive Greater Than Average
// https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

class Solution {
    fun smallestAbsent(nums: IntArray): Int {
        var s = HashSet<Int>()
        var sum = 0
        for (x in nums) {
            s.add(x)
            sum += x
        }
        var ans = maxOf(1, sum / nums.size + 1)
        while (s.contains(ans)) ans++
        return ans
    }
}
