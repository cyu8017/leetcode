// LeetCode 1975 - Maximum Matrix Sum
// https://leetcode.com/problems/maximum-matrix-sum/

func maxMatrixSum(matrix [][]int) int64 {
	var total int64
	neg := 0
	mn := int(1e9)
	for _, row := range matrix {
		for _, x := range row {
			if x < 0 {
				neg++
				x = -x
			}
			total += int64(x)
			if x < mn {
				mn = x
			}
		}
	}
	if neg%2 == 0 {
		return total
	}
	return total - 2*int64(mn)
}
