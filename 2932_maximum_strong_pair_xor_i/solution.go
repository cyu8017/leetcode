// LeetCode 2932 - Maximum Strong Pair XOR I
// https://leetcode.com/problems/maximum-strong-pair-xor-i/

func maximumStrongPairXor(nums []int) int {
	ans := 0
	for i := 0; i < len(nums); i++ {
		for j := i; j < len(nums); j++ {
			x, y := nums[i], nums[j]
			d := x - y
			if d < 0 {
				d = -d
			}
			mn := x
			if y < mn {
				mn = y
			}
			if d <= mn {
				xorr := x ^ y
				if xorr > ans {
					ans = xorr
				}
			}
		}
	}
	return ans
}
