// LeetCode 0659 - Split Array into Consecutive Subsequences
// https://leetcode.com/problems/split-array-into-consecutive-subsequences/

func isPossible(nums []int) bool {
	freq := map[int]int{}
	tails := map[int]int{}
	for _, num := range nums {
		freq[num]++
	}
	for _, num := range nums {
		if freq[num] == 0 {
			continue
		}
		freq[num]--
		if tails[num-1] > 0 {
			tails[num-1]--
			tails[num]++
		} else if freq[num+1] > 0 && freq[num+2] > 0 {
			freq[num+1]--
			freq[num+2]--
			tails[num+2]++
		} else {
			return false
		}
	}
	return true
}
