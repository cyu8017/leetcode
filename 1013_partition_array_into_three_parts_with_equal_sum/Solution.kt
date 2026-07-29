// LeetCode 1013 - Partition Array Into Three Parts With Equal Sum
// https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

class Solution {
    fun canThreePartsEqualSum(arr: IntArray): Boolean {
        val total = arr.sum()
        if (total % 3 != 0) return false
        val target = total / 3
        var parts = 0; var cur = 0
        for (x in arr) {
            cur += x
            if (cur == target) {
                parts++
                cur = 0
            }
        }
        return parts >= 3
    }
}
