// LeetCode 1013 - Partition Array Into Three Parts With Equal Sum
// https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

func canThreePartsEqualSum(arr []int) bool {
	total := 0
	for _, x := range arr {
		total += x
	}
	if total%3 != 0 {
		return false
	}
	target := total / 3
	parts, cur := 0, 0
	for _, x := range arr {
		cur += x
		if cur == target {
			parts++
			cur = 0
		}
	}
	return parts >= 3
}
