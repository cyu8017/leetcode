// LeetCode 1560 - Most Visited Sector in a Circular Track
// https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

func mostVisited(n int, rounds []int) []int {
	start, end := rounds[0], rounds[len(rounds)-1]
	if start <= end {
		ans := make([]int, 0, end-start+1)
		for i := start; i <= end; i++ {
			ans = append(ans, i)
		}
		return ans
	}
	ans := []int{}
	for i := 1; i <= end; i++ {
		ans = append(ans, i)
	}
	for i := start; i <= n; i++ {
		ans = append(ans, i)
	}
	return ans
}
