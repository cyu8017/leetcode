// LeetCode 3659 - Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/

func partitionArray(nums []int, k int) bool {
	n := len(nums)
	if n%k != 0 {
		return false
	}
	m := n / k
	mx := slices.Max(nums)
	cnt := make([]int, mx+1)
	for _, x := range nums {
		if cnt[x]++; cnt[x] > m {
			return false
		}
	}
	return true
}
