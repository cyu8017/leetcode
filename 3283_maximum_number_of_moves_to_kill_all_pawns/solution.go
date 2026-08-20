// LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
// https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

func maxMoves(kx int, ky int, positions [][]int) int {
	n := len(positions)
	pts := make([][2]int, n+1)
	pts[0] = [2]int{kx, ky}
	for i, p := range positions {
		pts[i+1] = [2]int{p[0], p[1]}
	}
	dist := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dist[i] = knightDist(pts[i][0], pts[i][1], pts)
	}
	N := 1 << n
	const neg = -1 << 30
	dp := make([][]int, N)
	for i := range dp {
		dp[i] = make([]int, n+1)
		for j := range dp[i] {
			dp[i][j] = neg
		}
	}
	dp[0][0] = 0
	for mask := 0; mask < N; mask++ {
		pc := bitsCount(mask)
		maximizing := pc%2 == 0 // Alice maximizes
		for cur := 0; cur <= n; cur++ {
			if dp[mask][cur] == neg {
				continue
			}
			for nxt := 0; nxt < n; nxt++ {
				if mask&(1<<nxt) != 0 {
					continue
				}
				nmask := mask | (1 << nxt)
				d := dist[cur][nxt+1]
				val := dp[mask][cur] + d
				if maximizing {
					if val > dp[nmask][nxt+1] {
						dp[nmask][nxt+1] = val
					}
				} else {
					if dp[nmask][nxt+1] == neg || val < dp[nmask][nxt+1] {
						dp[nmask][nxt+1] = val
					}
				}
			}
		}
	}
	// Actually minimax needs proper recursion. Use memoized game DP.
	return maxMovesGame(kx, ky, positions)
}

func maxMovesGame(kx, ky int, positions [][]int) int {
	n := len(positions)
	pts := make([][2]int, n+1)
	pts[0] = [2]int{kx, ky}
	for i, p := range positions {
		pts[i+1] = [2]int{p[0], p[1]}
	}
	dist := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dist[i] = knightDist(pts[i][0], pts[i][1], pts)
	}
	N := 1 << n
	memo := make([][]int, N)
	for i := range memo {
		memo[i] = make([]int, n+1)
		for j := range memo[i] {
			memo[i][j] = -1
		}
	}
	var dfs func(mask, cur, turn int) int
	dfs = func(mask, cur, turn int) int {
		if mask == N-1 {
			return 0
		}
		if memo[mask][cur] != -1 {
			return memo[mask][cur]
		}
		var best int
		if turn == 0 {
			best = -1 << 30
		} else {
			best = 1 << 30
		}
		for i := 0; i < n; i++ {
			if mask&(1<<i) != 0 {
				continue
			}
			d := dist[cur][i+1]
			v := d + dfs(mask|(1<<i), i+1, 1-turn)
			if turn == 0 {
				if v > best {
					best = v
				}
			} else if v < best {
				best = v
			}
		}
		memo[mask][cur] = best
		return best
	}
	return dfs(0, 0, 0)
}

func knightDist(x, y int, pts [][2]int) []int {
	dirs := [][2]int{{1, 2}, {1, -2}, {-1, 2}, {-1, -2}, {2, 1}, {2, -1}, {-2, 1}, {-2, -1}}
	type node struct{ x, y, d int }
	ans := make([]int, len(pts))
	for t := range pts {
		ans[t] = -1
	}
	vis := [50][50]bool{}
	q := []node{{x, y, 0}}
	vis[x][y] = true
	need := map[[2]int][]int{}
	for i, p := range pts {
		need[[2]int{p[0], p[1]}] = append(need[[2]int{p[0], p[1]}], i)
	}
	found := 0
	for len(q) > 0 && found < len(pts) {
		cur := q[0]
		q = q[1:]
		key := [2]int{cur.x, cur.y}
		if idxs, ok := need[key]; ok {
			for _, i := range idxs {
				if ans[i] == -1 {
					ans[i] = cur.d
					found++
				}
			}
		}
		for _, d := range dirs {
			nx, ny := cur.x+d[0], cur.y+d[1]
			if nx < 0 || ny < 0 || nx >= 50 || ny >= 50 || vis[nx][ny] {
				continue
			}
			vis[nx][ny] = true
			q = append(q, node{nx, ny, cur.d + 1})
		}
	}
	return ans
}

func bitsCount(x int) int {
	c := 0
	for x > 0 {
		c += x & 1
		x >>= 1
	}
	return c
}
