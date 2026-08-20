// LeetCode 2912 - Number of Ways to Reach Destination in the Grid
// https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/

func numberOfWays(n int, m int, k int, source []int, dest []int) int {
	const mod = 1_000_000_007
	// dp states: same cell, same row, same col, other
	sx, sy := source[0], source[1]
	tx, ty := dest[0], dest[1]
	var same, row, col, other int
	if sx == tx && sy == ty {
		same = 1
	} else if sx == tx {
		row = 1
	} else if sy == ty {
		col = 1
	} else {
		other = 1
	}
	for step := 0; step < k; step++ {
		ns := (row*(m-1) + col*(n-1)) % mod
		nr := (same + row*(m-2)%mod + other*(n-1)%mod) % mod
		nc := (same + col*(n-2)%mod + other*(m-1)%mod) % mod
		no := (row*(n-1) + col*(m-1) + other*(n+m-4)%mod) % mod
		same, row, col, other = ns, nr, nc, no
	}
	if sx == tx && sy == ty {
		return same
	}
	if sx == tx {
		return row
	}
	if sy == ty {
		return col
	}
	return other
}
