// LeetCode 3276 - Select Cells in Grid With Maximum Score
// https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

func maxScore(grid [][]int) int {
	m := len(grid)
	vals := map[int][]int{} // value -> rows containing it
	for i, row := range grid {
		seen := map[int]bool{}
		for _, v := range row {
			if !seen[v] {
				vals[v] = append(vals[v], i)
				seen[v] = true
			}
		}
	}
	type pair struct{ v, r int }
	arr := []int{}
	for v := range vals {
		arr = append(arr, v)
	}
	// sort desc
	for i := 0; i < len(arr); i++ {
		for j := i + 1; j < len(arr); j++ {
			if arr[j] > arr[i] {
				arr[i], arr[j] = arr[j], arr[i]
			}
		}
	}
	// DP on row mask
	N := 1 << m
	dp := make([]int, N)
	for _, v := range arr {
		ndp := append([]int(nil), dp...)
		for _, r := range vals[v] {
			bit := 1 << r
			for mask := 0; mask < N; mask++ {
				if mask&bit != 0 {
					continue
				}
				cand := dp[mask] + v
				nmask := mask | bit
				if cand > ndp[nmask] {
					ndp[nmask] = cand
				}
			}
		}
		dp = ndp
	}
	ans := 0
	for _, v := range dp {
		if v > ans {
			ans = v
		}
	}
	return ans
}
