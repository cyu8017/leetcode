// LeetCode 1899 - Merge Triplets to Form Target Triplet
// https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

func mergeTriplets(triplets [][]int, target []int) bool {
	merged := [3]int{0, 0, 0}
	for _, triplet := range triplets {
		if triplet[0] <= target[0] && triplet[1] <= target[1] && triplet[2] <= target[2] {
			if triplet[0] > merged[0] {
				merged[0] = triplet[0]
			}
			if triplet[1] > merged[1] {
				merged[1] = triplet[1]
			}
			if triplet[2] > merged[2] {
				merged[2] = triplet[2]
			}
		}
	}
	return merged[0] == target[0] && merged[1] == target[1] && merged[2] == target[2]
}
