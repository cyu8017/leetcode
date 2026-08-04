// LeetCode 1573 - Number of Ways to Split a String
// https://leetcode.com/problems/number-of-ways-to-split-a-string/

func numWays(s string) int {
	const MOD = 1_000_000_007
	ones := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			ones++
		}
	}
	if ones%3 != 0 {
		return 0
	}
	if ones == 0 {
		gaps := len(s) - 1
		return gaps * (gaps - 1) / 2 % MOD
	}
	target := ones / 3
	positions := []int{}
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			positions = append(positions, i)
		}
	}
	return (positions[target] - positions[target-1]) * (positions[2*target] - positions[2*target-1]) % MOD
}
