// LeetCode 0006 - Zigzag Conversion
// https://leetcode.com/problems/zigzag-conversion/

func convert(s string, numRows int) string {
	if numRows == 1 || numRows >= len(s) {
		return s
	}

	rows := make([][]byte, numRows)
	index := 0
	step := 1

	for i := 0; i < len(s); i++ {
		rows[index] = append(rows[index], s[i])
		if index == 0 {
			step = 1
		} else if index == numRows-1 {
			step = -1
		}
		index += step
	}

	result := make([]byte, 0, len(s))
	for _, row := range rows {
		result = append(result, row...)
	}
	return string(result)
}
