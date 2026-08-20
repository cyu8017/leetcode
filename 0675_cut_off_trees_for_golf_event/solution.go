// LeetCode 0675 - Cut Off Trees for Golf Event
// https://leetcode.com/problems/cut-off-trees-for-golf-event/

import "sort"

func cutOffTree(forest [][]int) int {
	m, n := len(forest), len(forest[0])
	type tree struct{ h, i, j int }
	trees := []tree{}
	for i, row := range forest {
		for j, h := range row {
			if h > 1 {
				trees = append(trees, tree{h, i, j})
			}
		}
	}
	sort.Slice(trees, func(a, b int) bool { return trees[a].h < trees[b].h })
	bfs := func(sr, sc, tr, tc int) int {
		if sr == tr && sc == tc {
			return 0
		}
		seen := map[[2]int]bool{{sr, sc}: true}
		type node struct{ r, c, dist int }
		queue := []node{{sr, sc, 0}}
		dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
		for len(queue) > 0 {
			cur := queue[0]
			queue = queue[1:]
			for _, d := range dirs {
				nr, nc := cur.r+d[0], cur.c+d[1]
				if nr < 0 || nr >= m || nc < 0 || nc >= n {
					continue
				}
				if seen[[2]int{nr, nc}] || forest[nr][nc] == 0 {
					continue
				}
				if nr == tr && nc == tc {
					return cur.dist + 1
				}
				seen[[2]int{nr, nc}] = true
				queue = append(queue, node{nr, nc, cur.dist + 1})
			}
		}
		return -1
	}
	sr, sc, steps := 0, 0, 0
	for _, t := range trees {
		dist := bfs(sr, sc, t.i, t.j)
		if dist < 0 {
			return -1
		}
		steps += dist
		sr, sc = t.i, t.j
	}
	return steps
}
