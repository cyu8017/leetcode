// LeetCode 2570 - Merge Two 2D Arrays by Summing Values
// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

class Solution {
    fun mergeArrays(nums1: Array<IntArray>, nums2: Array<IntArray>): Array<IntArray> {
        val ans = ArrayList<IntArray>()
        var i = 0
        var j = 0
        while (i < nums1.size && j < nums2.size) {
            when {
                nums1[i][0] == nums2[j][0] -> {
                    ans.add(intArrayOf(nums1[i][0], nums1[i][1] + nums2[j][1]))
                    i += 1
                    j += 1
                }
                nums1[i][0] < nums2[j][0] -> {
                    ans.add(intArrayOf(nums1[i][0], nums1[i][1]))
                    i += 1
                }
                else -> {
                    ans.add(intArrayOf(nums2[j][0], nums2[j][1]))
                    j += 1
                }
            }
        }
        while (i < nums1.size) {
            ans.add(intArrayOf(nums1[i][0], nums1[i][1]))
            i += 1
        }
        while (j < nums2.size) {
            ans.add(intArrayOf(nums2[j][0], nums2[j][1]))
            j += 1
        }
        return ans.toTypedArray()
    }
}
