// LeetCode 2155 - All Divisions With the Highest Score of a Binary Array
// https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

func maxScoreIndices(nums []int) []int {
	n := len(nums)
	total1 := 0
	for _, x := range nums {
		total1 += x
	}
	best, left0, right1 := total1, 0, total1
	ans := []int{0}
	for i := 0; i < n; i++ {
		if nums[i] == 0 {
			left0++
		} else {
			right1--
		}
		score := left0 + right1
		if score > best {
			best = score
			ans = []int{i + 1}
		} else if score == best {
			ans = append(ans, i+1)
		}
	}
	return ans
}
