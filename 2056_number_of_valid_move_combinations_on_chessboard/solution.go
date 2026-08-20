// LeetCode 2056 - Number of Valid Move Combinations On Chessboard
// https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

func countCombinations(pieces []string, positions [][]int) int {
	dirs := map[string][][2]int{
		"rook":   {{1, 0}, {-1, 0}, {0, 1}, {0, -1}},
		"bishop": {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}},
		"queen":  {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}},
	}
	n := len(pieces)
	type move struct {
		dr, dc, steps int
	}
	allMoves := make([][]move, n)
	for i, p := range pieces {
		ms := []move{{0, 0, 0}} // stay
		r, c := positions[i][0], positions[i][1]
		for _, d := range dirs[p] {
			nr, nc := r+d[0], c+d[1]
			step := 1
			for nr >= 1 && nr <= 8 && nc >= 1 && nc <= 8 {
				ms = append(ms, move{d[0], d[1], step})
				nr += d[0]
				nc += d[1]
				step++
			}
		}
		allMoves[i] = ms
	}
	chosen := make([]move, n)
	var okCombo func(int) bool
	okCombo = func(end int) bool {
		// simulate time 0..maxSteps
		maxT := 0
		for i := 0; i <= end; i++ {
			if chosen[i].steps > maxT {
				maxT = chosen[i].steps
			}
		}
		for t := 1; t <= maxT; t++ {
			pos := map[[2]int]int{}
			for i := 0; i <= end; i++ {
				m := chosen[i]
				steps := m.steps
				if steps == 0 {
					pr, pc := positions[i][0], positions[i][1]
					key := [2]int{pr, pc}
					if _, exists := pos[key]; exists {
						return false
					}
					pos[key] = i
					continue
				}
				use := t
				if use > steps {
					use = steps
				}
				pr := positions[i][0] + m.dr*use
				pc := positions[i][1] + m.dc*use
				key := [2]int{pr, pc}
				if _, exists := pos[key]; exists {
					return false
				}
				pos[key] = i
			}
		}
		return true
	}
	ans := 0
	var dfs func(int)
	dfs = func(i int) {
		if i == n {
			ans++
			return
		}
		for _, m := range allMoves[i] {
			chosen[i] = m
			if okCombo(i) {
				dfs(i + 1)
			}
		}
	}
	dfs(0)
	return ans
}
