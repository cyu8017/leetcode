// LeetCode 1301 - Number of Paths with Max Score
// https://leetcode.com/problems/number-of-paths-with-max-score/

func pathsWithMaxScore(board []string) []int {
	const mod = 1000000007
	n := len(board)
	score := make([][]int, n)
	ways := make([][]int, n)
	for i := 0; i < n; i++ {
		score[i] = make([]int, n)
		ways[i] = make([]int, n)
		for j := 0; j < n; j++ {
			score[i][j] = -1
		}
	}
	score[n-1][n-1] = 0
	ways[n-1][n-1] = 1
	for r := n - 1; r >= 0; r-- {
		for c := n - 1; c >= 0; c-- {
			if board[r][c] == 'X' || (r == n-1 && c == n-1) {
				continue
			}
			best, count := -1, 0
			for _, d := range [][2]int{{1, 0}, {0, 1}, {1, 1}} {
				nr, nc := r+d[0], c+d[1]
				if nr < n && nc < n && score[nr][nc] >= 0 {
					if score[nr][nc] > best {
						best = score[nr][nc]
						count = ways[nr][nc]
					} else if score[nr][nc] == best {
						count = (count + ways[nr][nc]) % mod
					}
				}
			}
			if best >= 0 {
				ch := board[r][c]
				add := 0
				if ch >= '0' && ch <= '9' {
					add = int(ch - '0')
				}
				score[r][c] = best + add
				ways[r][c] = count
			}
		}
	}
	s := score[0][0]
	if s < 0 {
		s = 0
	}
	return []int{s, ways[0][0]}
}
