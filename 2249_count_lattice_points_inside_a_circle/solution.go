// LeetCode 2249 - Count Lattice Points Inside a Circle
// https://leetcode.com/problems/count-lattice-points-inside-a-circle/

func countLatticePoints(circles [][]int) int {
	seen := map[[2]int]bool{}
	for _, c := range circles {
		x, y, r := c[0], c[1], c[2]
		for i := x - r; i <= x+r; i++ {
			for j := y - r; j <= y+r; j++ {
				if (i-x)*(i-x)+(j-y)*(j-y) <= r*r {
					seen[[2]int{i, j}] = true
				}
			}
		}
	}
	return len(seen)
}
