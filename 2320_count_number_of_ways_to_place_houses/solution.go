// LeetCode 2320 - Count Number of Ways to Place Houses
// https://leetcode.com/problems/count-number-of-ways-to-place-houses/

func countHousePlacements(n int) int {
	const mod = 1000000007
	a, b := 1, 1 // empty ends, house ends for one side length i
	for i := 1; i <= n; i++ {
		a, b = (a+b)%mod, a
	}
	ways := (a + b) % mod
	return int(int64(ways) * int64(ways) % mod)
}
