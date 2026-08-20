// LeetCode 0749 - Contain Virus
// https://leetcode.com/problems/contain-virus/

func containVirus(isInfected [][]int) int {
	m, n := len(isInfected), len(isInfected[0])
	walls := 0
	neighbors := func(r, c int) [][2]int {
		out := [][2]int{}
		for _, d := range [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} {
			nr, nc := r+d[0], c+d[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n {
				out = append(out, [2]int{nr, nc})
			}
		}
		return out
	}
	for {
		seen := map[[2]int]bool{}
		regions := []map[[2]int]bool{}
		frontiers := []map[[2]int]bool{}
		perimeters := []int{}
		for i := 0; i < m; i++ {
			for j := 0; j < n; j++ {
				if isInfected[i][j] == 1 && !seen[[2]int{i, j}] {
					stack := [][2]int{{i, j}}
					seen[[2]int{i, j}] = true
					region := map[[2]int]bool{}
					frontier := map[[2]int]bool{}
					perimeter := 0
					for len(stack) > 0 {
						cur := stack[len(stack)-1]
						stack = stack[:len(stack)-1]
						r, c := cur[0], cur[1]
						region[[2]int{r, c}] = true
						for _, nb := range neighbors(r, c) {
							nr, nc := nb[0], nb[1]
							if isInfected[nr][nc] == 1 && !seen[[2]int{nr, nc}] {
								seen[[2]int{nr, nc}] = true
								stack = append(stack, [2]int{nr, nc})
							} else if isInfected[nr][nc] == 0 {
								frontier[[2]int{nr, nc}] = true
								perimeter++
							}
						}
					}
					regions = append(regions, region)
					frontiers = append(frontiers, frontier)
					perimeters = append(perimeters, perimeter)
				}
			}
		}
		if len(regions) == 0 {
			break
		}
		quarantine := 0
		for i := 1; i < len(regions); i++ {
			if len(frontiers[i]) > len(frontiers[quarantine]) {
				quarantine = i
			}
		}
		if len(frontiers[quarantine]) == 0 {
			break
		}
		walls += perimeters[quarantine]
		for cell := range regions[quarantine] {
			isInfected[cell[0]][cell[1]] = -1
		}
		for index, frontier := range frontiers {
			if index == quarantine {
				continue
			}
			for cell := range frontier {
				isInfected[cell[0]][cell[1]] = 1
			}
		}
	}
	return walls
}
