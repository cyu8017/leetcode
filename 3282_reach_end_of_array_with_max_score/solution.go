// LeetCode 3282 - Reach End of Array With Max Score
// https://leetcode.com/problems/reach-end-of-array-with-max-score/

func findMaximumScore(nums []int) int64 {
	var ans int64
	maxV := 0
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] > maxV {
			maxV = nums[i]
		}
		ans += int64(maxV)
	}
	return ans
}
