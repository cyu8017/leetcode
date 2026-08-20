// LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
// https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

func maxTrailingZeros(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	type pair struct{ two, five int }
	fact := func(x int) pair {
		t, f := 0, 0
		for x%2 == 0 {
			t++
			x /= 2
		}
		for x%5 == 0 {
			f++
			x /= 5
		}
		return pair{t, f}
	}
	left := make([][]pair, m)
	up := make([][]pair, m)
	for i := 0; i < m; i++ {
		left[i] = make([]pair, n)
		up[i] = make([]pair, n)
		for j := 0; j < n; j++ {
			p := fact(grid[i][j])
			left[i][j] = p
			up[i][j] = p
			if j > 0 {
				left[i][j].two += left[i][j-1].two
				left[i][j].five += left[i][j-1].five
			}
			if i > 0 {
				up[i][j].two += up[i-1][j].two
				up[i][j].five += up[i-1][j].five
			}
		}
	}
	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}
	ans := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			cell := fact(grid[i][j])
			// four corner paths through (i,j)
			L := left[i][j]
			Rtwo, Rfive := left[i][n-1].two-left[i][j].two+cell.two, left[i][n-1].five-left[i][j].five+cell.five
			U := up[i][j]
			Dtwo, Dfive := up[m-1][j].two-up[i][j].two+cell.two, up[m-1][j].five-up[i][j].five+cell.five
			cands := []pair{
				{L.two + U.two - cell.two, L.five + U.five - cell.five},
				{L.two + Dtwo - cell.two, L.five + Dfive - cell.five},
				{Rtwo + U.two - cell.two, Rfive + U.five - cell.five},
				{Rtwo + Dtwo - cell.two, Rfive + Dfive - cell.five},
			}
			for _, c := range cands {
				z := min(c.two, c.five)
				if z > ans {
					ans = z
				}
			}
		}
	}
	return ans
}
