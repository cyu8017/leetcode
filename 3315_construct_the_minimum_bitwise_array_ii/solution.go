// LeetCode 3315 - Construct the Minimum Bitwise Array II
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

func minBitwiseArray(nums []int) []int {
	ans := make([]int, len(nums))
	for i, n := range nums {
		if n == 2 {
			ans[i] = -1
			continue
		}
		// find lowest 0-bit streak in binary of n ending... 
		// x|(x+1)==n => x = n with trailing 1s pattern
		ans[i] = -1
		for b := 0; b < 31; b++ {
			if (n>>b)&1 == 0 {
				continue
			}
			x := n ^ (1 << b)
			if x|(x+1) == n {
				ans[i] = x
				break
			}
		}
	}
	return ans
}
