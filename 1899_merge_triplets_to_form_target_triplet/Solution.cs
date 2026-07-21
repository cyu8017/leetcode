// LeetCode 1899 - Merge Triplets to Form Target Triplet
// https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

public class Solution {
    public bool MergeTriplets(int[][] triplets, int[] target) {
        var merged = new int[3];
        foreach (var t in triplets) {
            if (t[0] <= target[0] && t[1] <= target[1] && t[2] <= target[2]) {
                merged[0] = Math.Max(merged[0], t[0]);
                merged[1] = Math.Max(merged[1], t[1]);
                merged[2] = Math.Max(merged[2], t[2]);
            }
        }
        return merged[0] == target[0] && merged[1] == target[1] && merged[2] == target[2];
    }
}
