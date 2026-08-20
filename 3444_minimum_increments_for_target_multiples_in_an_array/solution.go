// LeetCode 3444 - Minimum Increments for Target Multiples in an Array
// https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

func minimumIncrements(nums []int, target []int) int {
	m := len(target)
	N := 1 << m
	const inf = int(1e18)
	dp := make([]int, N)
	for i := range dp {
		dp[i] = inf
	}
	dp[0] = 0
	for _, x := range nums {
		ndp := append([]int(nil), dp...)
		for mask := 0; mask < N; mask++ {
			// assign x (after increment) to cover subset of targets
			for sub := 1; sub < N; sub++ {
				lcm := 1
				ok := true
				for i := 0; i < m; i++ {
					if sub&(1<<i) != 0 {
						lcm = lcm3444(lcm, target[i])
						if lcm > 1e9 {
							ok = false
							break
						}
					}
				}
				if !ok {
					continue
				}
				// cost to make x multiple of lcm
				cost := (lcm - x%lcm) % lcm
				nmask := mask | sub
				if dp[mask]+cost < ndp[nmask] {
					ndp[nmask] = dp[mask] + cost
				}
			}
		}
		dp = ndp
	}
	return dp[N-1]
}

func gcd3444(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
func lcm3444(a, b int) int {
	return a / gcd3444(a, b) * b
}
