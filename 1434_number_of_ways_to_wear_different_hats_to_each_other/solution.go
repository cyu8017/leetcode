// LeetCode 1434 - Number of Ways to Wear Different Hats to Each Other
// https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/

func numberWays(hats [][]int) int {
	const mod = 1000000007
	people := len(hats)
	wearers := make([][]int, 41)
	for person, choices := range hats {
		for _, hat := range choices {
			wearers[hat] = append(wearers[hat], person)
		}
	}
	dp := make([]int, 1<<people)
	dp[0] = 1
	for hat := 1; hat <= 40; hat++ {
		nxt := append([]int(nil), dp...)
		for mask, ways := range dp {
			if ways == 0 {
				continue
			}
			for _, person := range wearers[hat] {
				if mask>>person&1 == 0 {
					nxt[mask|(1<<person)] = (nxt[mask|(1<<person)] + ways) % mod
				}
			}
		}
		dp = nxt
	}
	return dp[(1<<people)-1]
}
