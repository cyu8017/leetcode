// LeetCode 2956 - Find Common Elements Between Two Arrays
// https://leetcode.com/problems/find-common-elements-between-two-arrays/

class Solution {
    fun findIntersectionValues(nums1: IntArray, nums2: IntArray): IntArray {
        var s1 = HashSet<Int>()
        var s2 = HashSet<Int>()
        for (v in nums1) { s1.add(v) }
        for (v in nums2) { s2.add(v) }
        var a = 0
        var b = 0
        for (v in nums1) { if (s2.contains(v)) a++ }
        for (v in nums2) { if (s1.contains(v)) b++ }
        return intArrayOf( a, b )
    }
}
