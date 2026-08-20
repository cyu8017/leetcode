// LeetCode 2206 - Divide Array Into Equal Pairs
// https://leetcode.com/problems/divide-array-into-equal-pairs/

func divideArray(nums []int) bool {
	freq := map[int]int{}
	for _, x := range nums {
		freq[x]++
	}
	for _, c := range freq {
		if c%2 != 0 {
			return false
		}
	}
	return true
}
