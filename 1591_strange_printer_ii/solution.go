// LeetCode 1591 - Strange Printer II
// https://leetcode.com/problems/strange-printer-ii/

func isPrintable(targetGrid [][]int) bool {
	colors := map[int]bool{}
	bounds := map[int][4]int{}
	for r, row := range targetGrid {
		for col, c := range row {
			colors[c] = true
			b, ok := bounds[c]
			if !ok {
				bounds[c] = [4]int{r, col, r, col}
			} else {
				if r < b[0] {
					b[0] = r
				}
				if col < b[1] {
					b[1] = col
				}
				if r > b[2] {
					b[2] = r
				}
				if col > b[3] {
					b[3] = col
				}
				bounds[c] = b
			}
		}
	}
	graph := map[int]map[int]bool{}
	indegree := map[int]int{}
	for c := range colors {
		graph[c] = map[int]bool{}
		indegree[c] = 0
	}
	for c, b := range bounds {
		for r := b[0]; r <= b[2]; r++ {
			for col := b[1]; col <= b[3]; col++ {
				other := targetGrid[r][col]
				if other != c && !graph[c][other] {
					graph[c][other] = true
					indegree[other]++
				}
			}
		}
	}
	queue := []int{}
	for c := range colors {
		if indegree[c] == 0 {
			queue = append(queue, c)
		}
	}
	seen := 0
	for len(queue) > 0 {
		c := queue[0]
		queue = queue[1:]
		seen++
		for nxt := range graph[c] {
			indegree[nxt]--
			if indegree[nxt] == 0 {
				queue = append(queue, nxt)
			}
		}
	}
	return seen == len(colors)
}
