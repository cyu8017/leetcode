// LeetCode 3046 - Split the Array
// https://leetcode.com/problems/split-the-array/

func isPossibleToSplit(nums []int) bool {
	cnt := [101]int{}
	for _, x := range nums {
		cnt[x]++
		if cnt[x] >= 3 {
			return false
		}
	}
	return true
}
