// LeetCode 1868 - Product of Two Run-Length Encoded Arrays
// https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

func findRLEArray(encoded1 [][]int, encoded2 [][]int) [][]int {
	result := make([][]int, 0)
	i, j := 0, 0
	rem1 := encoded1[0][1]
	rem2 := encoded2[0][1]

	for i < len(encoded1) {
		take := rem1
		if rem2 < take {
			take = rem2
		}
		value := encoded1[i][0] * encoded2[j][0]
		if len(result) > 0 && result[len(result)-1][0] == value {
			result[len(result)-1][1] += take
		} else {
			result = append(result, []int{value, take})
		}

		rem1 -= take
		rem2 -= take
		if rem1 == 0 {
			i++
			if i < len(encoded1) {
				rem1 = encoded1[i][1]
			}
		}
		if rem2 == 0 {
			j++
			if j < len(encoded2) {
				rem2 = encoded2[j][1]
			}
		}
	}

	return result
}
