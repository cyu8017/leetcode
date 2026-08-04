// LeetCode 1985
// https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution {
    fun kthLargestNumber(nums: Array<String>, k: Int): String =
        nums.sortedWith(compareByDescending<String> { it.length }.thenByDescending { it })[k - 1]
}
