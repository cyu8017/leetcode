// LeetCode 0532 - K-diff Pairs in an Array
// https://leetcode.com/problems/k-diff-pairs-in-an-array/

func findPairs(nums []int, k int) int {
	if k < 0 {
		return 0
	}

	freq := make(map[int]int)
	for _, num := range nums {
		freq[num]++
	}

	pairs := 0
	for num, count := range freq {
		if k == 0 {
			if count > 1 {
				pairs++
			}
		} else if _, ok := freq[num+k]; ok {
			pairs++
		}
	}
	return pairs
}
