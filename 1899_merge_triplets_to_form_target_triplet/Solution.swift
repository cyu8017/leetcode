// LeetCode 1899 - Merge Triplets to Form Target Triplet
// https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

class Solution {
    func mergeTriplets(_ triplets: [[Int]], _ target: [Int]) -> Bool {
        var merged = [0, 0, 0]
        for triplet in triplets {
            let a = triplet[0]
            let b = triplet[1]
            let c = triplet[2]
            if a <= target[0] && b <= target[1] && c <= target[2] {
                merged[0] = max(merged[0], a)
                merged[1] = max(merged[1], b)
                merged[2] = max(merged[2], c)
            }
        }
        return merged == target
    }
}
