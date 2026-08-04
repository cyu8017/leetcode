// LeetCode 1583 - Count Unhappy Friends
// https://leetcode.com/problems/count-unhappy-friends/

func unhappyFriends(n int, preferences [][]int, pairs [][]int) int {
	rank := make([][]int, n)
	for i := 0; i < n; i++ {
		rank[i] = make([]int, n)
		for j, friend := range preferences[i] {
			rank[i][friend] = j
		}
	}
	partner := make([]int, n)
	for _, p := range pairs {
		a, b := p[0], p[1]
		partner[a], partner[b] = b, a
	}
	unhappy := 0
	for x := 0; x < n; x++ {
		y := partner[x]
		for _, u := range preferences[x][:rank[x][y]] {
			if rank[u][x] < rank[u][partner[u]] {
				unhappy++
				break
			}
		}
	}
	return unhappy
}
