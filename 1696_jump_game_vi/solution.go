// LeetCode 1696 - Jump Game VI
// https://leetcode.com/problems/jump-game-vi/

func maxResult(nums []int, k int) int {
	type pair struct{ i, score int }
	q := []pair{{0, nums[0]}}
	for i := 1; i < len(nums); i++ {
		for q[0].i < i-k {
			q = q[1:]
		}
		score := nums[i] + q[0].score
		for len(q) > 0 && q[len(q)-1].score <= score {
			q = q[:len(q)-1]
		}
		q = append(q, pair{i, score})
	}
	return q[len(q)-1].score
}
