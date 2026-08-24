// LeetCode 3002 - Maximum Size of a Set After Removals
// https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

class Solution {
    fun maximumSetSize(nums1: IntArray, nums2: IntArray): Int {
        var s1 = HashSet<Int>()
        var s2 = HashSet<Int>()
        for (v in nums1) { s1.add(v) }
        for (v in nums2) { s2.add(v) }
        var a = 0
        var b = 0
        var c = 0
        for (x in s1) { if (!s2.contains(x)) a++ }
        for (x in s2) {
            if (!s1.contains(x)) b++
            else c++
        }
        var n = nums1.size
        a = minOf(a, n / 2)
        b = minOf(b, n / 2)
        return minOf(a + b + c, n)
    }
}
