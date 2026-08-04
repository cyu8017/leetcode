// LeetCode 1460 - Make Two Arrays Equal by Reversing Subarrays
// https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

class Solution {
    fun canBeEqual(target: IntArray, arr: IntArray): Boolean {
        val a = target.copyOf().also { it.sort() }
        val b = arr.copyOf().also { it.sort() }
        return a.contentEquals(b)
    }
}
