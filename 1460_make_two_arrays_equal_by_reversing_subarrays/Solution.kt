// LeetCode 1460 - Make Two Arrays Equal by Reversing Subarrays
// https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

class Solution {
    fun canBeEqual(target: IntArray, arr: IntArray): Boolean {
        return target.sorted() == arr.sorted()
    }
}
