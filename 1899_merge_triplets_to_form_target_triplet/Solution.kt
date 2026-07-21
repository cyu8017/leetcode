// LeetCode 1899 - Merge Triplets to Form Target Triplet
// https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

class Solution {
    fun mergeTriplets(triplets: Array<IntArray>, target: IntArray): Boolean {
        val merged = IntArray(3)
        for (t in triplets) {
            if (t[0] <= target[0] && t[1] <= target[1] && t[2] <= target[2]) {
                merged[0] = maxOf(merged[0], t[0])
                merged[1] = maxOf(merged[1], t[1])
                merged[2] = maxOf(merged[2], t[2])
            }
        }
        return merged.contentEquals(target)
    }
}
