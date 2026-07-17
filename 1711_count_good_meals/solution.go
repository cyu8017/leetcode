// LeetCode 1711 - Count Good Meals
// https://leetcode.com/problems/count-good-meals/

func countPairs(deliciousness []int) int {
	const mod = 1000000007
	seen := make(map[int]int64)
	var ans int64
	for _, value := range deliciousness {
		for power := 0; power < 22; power++ {
			if count, ok := seen[(1<<power)-value]; ok {
				ans += count
			}
		}
		seen[value]++
	}
	return int(ans % mod)
}
