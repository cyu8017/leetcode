// LeetCode 4011 - Count Subarrays With Even Odd Ratio I
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/

func countRatioSubarrays(nums []int, a int, b int) int {
	n := len(nums)
	var ans int64 = 0

	for i := 0; i < n; i++ {
		y := 0

		for j := i; j < n; j++ {
			y += nums[j] % 2
			x := j - i + 1 - y

			if y > 0 && int64(x)*int64(b) <= int64(y)*int64(a) {
				ans++
			}
		}
	}

	return int(ans)
}
