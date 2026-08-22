// LeetCode 3981 - Count Distinct Ways to Form Target from Two Strings
// https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/

func countWays(word1 string, word2 string, target string) int {
	const mod = 1000000007
	n1, n2 := len(word1), len(word2)
	size := (n1 + 1) * (n2 + 1) * 4
	index := func(i, j, mask int) int {
		return ((i*(n2+1)+j)*4 + mask)
	}
	dp := make([]int, size)
	dp[index(0, 0, 0)] = 1
	for t := 0; t < len(target); t++ {
		next := make([]int, size)
		for j := 0; j <= n2; j++ {
			prefix := [4]int{}
			for a := 0; a < n1; a++ {
				for mask := 0; mask < 4; mask++ {
					prefix[mask] += dp[index(a, j, mask)]
					if prefix[mask] >= mod {
						prefix[mask] -= mod
					}
				}
				if word1[a] == target[t] {
					for mask := 0; mask < 4; mask++ {
						at := index(a+1, j, mask|1)
						next[at] += prefix[mask]
						if next[at] >= mod {
							next[at] -= mod
						}
					}
				}
			}
		}
		for i := 0; i <= n1; i++ {
			prefix := [4]int{}
			for b := 0; b < n2; b++ {
				for mask := 0; mask < 4; mask++ {
					prefix[mask] += dp[index(i, b, mask)]
					if prefix[mask] >= mod {
						prefix[mask] -= mod
					}
				}
				if word2[b] == target[t] {
					for mask := 0; mask < 4; mask++ {
						at := index(i, b+1, mask|2)
						next[at] += prefix[mask]
						if next[at] >= mod {
							next[at] -= mod
						}
					}
				}
			}
		}
		dp = next
	}
	answer := 0
	for i := 0; i <= n1; i++ {
		for j := 0; j <= n2; j++ {
			answer += dp[index(i, j, 3)]
			if answer >= mod {
				answer -= mod
			}
		}
	}
	return answer
}