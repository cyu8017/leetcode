// LeetCode 0922 - Sort Array By Parity II
// https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution {
    fun sortArrayByParityII(nums: IntArray): IntArray {
        var n = nums.size
        var ans = IntArray(n)
        var even = 0
        var odd = 1
        for (x in nums) {
            if (x % 2 == 0) { ans[even] = x; even += 2; }
            else { ans[odd] = x; odd += 2; }
        }
        return ans
    }
}
