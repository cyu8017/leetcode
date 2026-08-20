// LeetCode 2184 - Number of Ways to Build Sturdy Brick Wall
// https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

func buildWall(height int, width int, bricks []int) int {
	const MOD = 1_000_000_007
	masks := []int{}
	var gen func(remain, mask int)
	gen = func(remain, mask int) {
		if remain == 0 {
			masks = append(masks, mask)
			return
		}
		for _, b := range bricks {
			if b <= remain {
				nm := mask
				if remain-b > 0 {
					nm |= 1 << (remain - b)
				}
				gen(remain-b, nm)
			}
		}
	}
	gen(width, 0)
	m := len(masks)
	compat := make([][]int, m)
	for i := 0; i < m; i++ {
		for j := 0; j < m; j++ {
			if masks[i]&masks[j] == 0 {
				compat[i] = append(compat[i], j)
			}
		}
	}
	dp := make([]int, m)
	for i := range dp {
		dp[i] = 1
	}
	for h := 1; h < height; h++ {
		ndp := make([]int, m)
		for i := 0; i < m; i++ {
			for _, j := range compat[i] {
				ndp[j] = (ndp[j] + dp[i]) % MOD
			}
		}
		dp = ndp
	}
	ans := 0
	for _, v := range dp {
		ans = (ans + v) % MOD
	}
	return ans
}
