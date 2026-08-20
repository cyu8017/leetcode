// LeetCode 2219 - Maximum Sum Score of Array
// https://leetcode.com/problems/maximum-sum-score-of-array/

func maximumSumScore(nums []int) int64 {
	var total, pref int64
	for _, x := range nums {
		total += int64(x)
	}
	ans := int64(-1 << 63)
	for _, x := range nums {
		pref += int64(x)
		score := pref
		if total-pref+int64(x) > score {
			score = total - pref + int64(x)
		}
		if score > ans {
			ans = score
		}
	}
	return ans
}
