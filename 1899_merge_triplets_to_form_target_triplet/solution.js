// LeetCode 1899 - Merge Triplets to Form Target Triplet
// https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

/**
 * @param {number[][]} triplets
 * @param {number[]} target
 * @return {boolean}
 */
var mergeTriplets = function(triplets, target) {
    const merged = [0, 0, 0];
    for (const [a, b, c] of triplets) {
        if (a <= target[0] && b <= target[1] && c <= target[2]) {
            merged[0] = Math.max(merged[0], a);
            merged[1] = Math.max(merged[1], b);
            merged[2] = Math.max(merged[2], c);
        }
    }
    return merged[0] === target[0] && merged[1] === target[1] && merged[2] === target[2];
};
