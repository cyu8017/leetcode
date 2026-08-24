// LeetCode 0760 - Find Anagram Mappings
// https://leetcode.com/problems/find-anagram-mappings/

class Solution {
    fun anagramMappings(nums1: IntArray, nums2: IntArray): IntArray {
        val positions = HashMap<Int, ArrayDeque<Int>>()
        for (i in nums2.indices) {
            positions.getOrPut(nums2[i]) { ArrayDeque() }.add(i)
        }
        val result = IntArray(nums1.size)
        for (i in nums1.indices) {
            result[i] = positions[nums1[i]]!!.removeFirst()
        }
        return result
    }
}
