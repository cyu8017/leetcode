// LeetCode 1072 - Flip Columns For Maximum Number of Equal Rows
// https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

func maxEqualRowsAfterFlips(matrix [][]int) int {
	patterns := map[string]int{}
	best := 0
	for _, row := range matrix {
		base := row[0]
		buf := make([]byte, len(row))
		for i, x := range row {
			buf[i] = byte('0' + (x ^ base))
		}
		key := string(buf)
		patterns[key]++
		if patterns[key] > best {
			best = patterns[key]
		}
	}
	return best
}
