// LeetCode 2786 - Visit Array Positions to Maximize Score
// https://leetcode.com/problems/visit-array-positions-to-maximize-score/

func maxScore(nums []int, x int) int64 {
	n := len(nums)
	even := int64(nums[0])
	odd := int64(nums[0])
	if nums[0]%2 == 0 {
		odd = int64(-1 << 60)
	} else {
		even = int64(-1 << 60)
	}
	for i := 1; i < n; i++ {
		v := int64(nums[i])
		if nums[i]%2 == 0 {
			even = max64(even+v, odd+v-int64(x))
		} else {
			odd = max64(odd+v, even+v-int64(x))
		}
	}
	return max64(even, odd)
}

func max64(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}
