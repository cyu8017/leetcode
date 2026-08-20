// LeetCode 0874 - Walking Robot Simulation
// https://leetcode.com/problems/walking-robot-simulation/

func robotSim(commands []int, obstacles [][]int) int {
	blocked := map[[2]int]bool{}
	for _, o := range obstacles {
		blocked[[2]int{o[0], o[1]}] = true
	}
	dirs := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	x, y, d, best := 0, 0, 0, 0
	for _, cmd := range commands {
		if cmd == -1 {
			d = (d + 1) % 4
		} else if cmd == -2 {
			d = (d + 3) % 4
		} else {
			dx, dy := dirs[d][0], dirs[d][1]
			for step := 0; step < cmd; step++ {
				nx, ny := x+dx, y+dy
				if blocked[[2]int{nx, ny}] {
					break
				}
				x, y = nx, ny
			}
			if x*x+y*y > best {
				best = x*x + y*y
			}
		}
	}
	return best
}
