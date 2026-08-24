// LeetCode 3866 - First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/

class Solution {
    fun firstUniqueEven(nums: IntArray): Int {
        var cnt = IntArray(101)
        for (x in nums) { cnt[x]++ }
        for (x in nums) {
            if (x % 2 == 0 && cnt[x] == 1) return x
        }
        return -1
    }
}
