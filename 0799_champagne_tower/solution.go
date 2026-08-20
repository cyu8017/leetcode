// LeetCode 0799 - Champagne Tower
// https://leetcode.com/problems/champagne-tower/

func champagneTower(poured int, query_row int, query_glass int) float64 {
	row := []float64{float64(poured)}
	for r := 0; r < query_row; r++ {
		next := make([]float64, r+2)
		for i, amount := range row {
			overflow := (amount - 1.0) / 2.0
			if overflow > 0 {
				next[i] += overflow
				next[i+1] += overflow
			}
		}
		row = next
	}
	if row[query_glass] > 1.0 {
		return 1.0
	}
	return row[query_glass]
}
