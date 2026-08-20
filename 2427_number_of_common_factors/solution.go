// LeetCode 2427 - Number of Common Factors
// https://leetcode.com/problems/number-of-common-factors/

func commonFactors(a int, b int) int {
	g := a
	for b != 0 {
		g, b = b, g%b
	}
	ans := 0
	for i := 1; i*i <= g; i++ {
		if g%i == 0 {
			ans++
			if i*i != g {
				ans++
			}
		}
	}
	return ans
}
