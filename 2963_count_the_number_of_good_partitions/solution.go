// LeetCode 2963 - Count the Number of Good Partitions
// https://leetcode.com/problems/count-the-number-of-good-partitions/

func numberOfGoodPartitions(nums []int) int {
	const mod = 1_000_000_007
	last := map[int]int{}
	for i, v := range nums {
		last[v] = i
	}
	ans := 1
	end := 0
	for i, v := range nums {
		if last[v] > end {
			end = last[v]
		}
		if i == end && i != len(nums)-1 {
			ans = ans * 2 % mod
		}
	}
	return ans
}
