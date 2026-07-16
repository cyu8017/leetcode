// LeetCode 0416 - Partition Equal Subset Sum
// https://leetcode.com/problems/partition-equal-subset-sum/

func canPartition(nums []int) bool {
	total := 0
	for _, value := range nums {
		total += value
	}
	if total%2 != 0 {
		return false
	}

	target := total / 2
	possible := map[int]bool{0: true}

	for _, value := range nums {
		next := make(map[int]bool, len(possible))
		for amount := range possible {
			next[amount] = true
			if amount+value <= target {
				next[amount+value] = true
			}
		}
		possible = next
		if possible[target] {
			return true
		}
	}

	return possible[target]
}
