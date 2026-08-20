// LeetCode 2147 - Number of Ways to Divide a Long Corridor
// https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

func numberOfWays(corridor string) int {
	const MOD = 1_000_000_007
	seats := []int{}
	for i := 0; i < len(corridor); i++ {
		if corridor[i] == 'S' {
			seats = append(seats, i)
		}
	}
	if len(seats) == 0 || len(seats)%2 != 0 {
		return 0
	}
	ans := 1
	for i := 2; i < len(seats); i += 2 {
		ans = ans * (seats[i] - seats[i-1]) % MOD
	}
	return ans
}
