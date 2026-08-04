// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

class Solution {
    fun maximumSum(arr: IntArray): Int {
        var keep = arr[0]
        var delete = arr[0]
        var ans = arr[0]
        for (i in 1 until arr.size) {
            val x = arr[i]
            delete = maxOf(keep, delete + x)
            keep = maxOf(keep + x, x)
            ans = maxOf(ans, keep, delete)
        }
        return ans
    }
}
