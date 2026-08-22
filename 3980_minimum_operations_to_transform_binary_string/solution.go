// LeetCode 3980 - Minimum Operations to Transform Binary String
// https://leetcode.com/problems/minimum-operations-to-transform-binary-string/

func minOperations(s1 string, s2 string) int {
	const infinity = int(1e9)
	dp := [2]int{0, infinity}
	for i := 0; i < len(s1); i++ {
		next := [2]int{infinity, infinity}
		for forcedZero := 0; forcedZero <= 1; forcedZero++ {
			if dp[forcedZero] == infinity {
				continue
			}
			current := s1[i]
			if forcedZero == 1 {
				current = '0'
			}

			direct := dp[forcedZero]
			if current == '0' && s2[i] == '1' {
				direct++
			} else if current == '1' && s2[i] == '0' {
				direct = infinity
			}
			if direct < next[0] {
				next[0] = direct
			}

			if i+1 < len(s1) {
				cost := dp[forcedZero] + 1
				if current == '0' {
					cost++
				}
				if s1[i+1] == '0' {
					cost++
				}
				if s2[i] == '1' {
					cost++
				}
				if cost < next[1] {
					next[1] = cost
				}
			}
		}
		dp = next
	}
	if dp[0] == infinity {
		return -1
	}
	return dp[0]
}