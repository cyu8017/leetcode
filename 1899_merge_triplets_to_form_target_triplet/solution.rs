// LeetCode 1899 - Merge Triplets to Form Target Triplet
// https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

impl Solution {
    pub fn merge_triplets(triplets: Vec<Vec<i32>>, target: Vec<i32>) -> bool {
        let mut merged = [0, 0, 0];
        for t in &triplets {
            if t[0] <= target[0] && t[1] <= target[1] && t[2] <= target[2] {
                merged[0] = merged[0].max(t[0]);
                merged[1] = merged[1].max(t[1]);
                merged[2] = merged[2].max(t[2]);
            }
        }
        merged[0] == target[0] && merged[1] == target[1] && merged[2] == target[2]
    }
}
