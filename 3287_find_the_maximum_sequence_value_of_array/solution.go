// LeetCode 3287 - Find the Maximum Sequence Value of Array
// https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

func maxValue(nums []int, k int) int {
	n := len(nums)
	const MAX = 128
	// left[i][j][v] = possible OR using j elements from first i
	left := make([][][]bool, n+1)
	for i := range left {
		left[i] = make([][]bool, k+1)
		for j := range left[i] {
			left[i][j] = make([]bool, MAX)
		}
	}
	left[0][0][0] = true
	for i := 0; i < n; i++ {
		for j := 0; j <= k; j++ {
			for v := 0; v < MAX; v++ {
				if !left[i][j][v] {
					continue
				}
				left[i+1][j][v] = true
				if j < k {
					left[i+1][j+1][v|nums[i]] = true
				}
			}
		}
	}
	right := make([][][]bool, n+1)
	for i := range right {
		right[i] = make([][]bool, k+1)
		for j := range right[i] {
			right[i][j] = make([]bool, MAX)
		}
	}
	right[n][0][0] = true
	for i := n - 1; i >= 0; i-- {
		for j := 0; j <= k; j++ {
			for v := 0; v < MAX; v++ {
				if !right[i+1][j][v] {
					continue
				}
				right[i][j][v] = true
				if j < k {
					right[i][j+1][v|nums[i]] = true
				}
			}
		}
	}
	ans := 0
	for mid := k; mid+k <= n; mid++ {
		for a := 0; a < MAX; a++ {
			if !left[mid][k][a] {
				continue
			}
			for b := 0; b < MAX; b++ {
				if right[mid][k][b] {
					if a^b > ans {
						ans = a ^ b
					}
				}
			}
		}
	}
	return ans
}
