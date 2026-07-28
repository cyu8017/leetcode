// LeetCode 1089 - Duplicate Zeros
// https://leetcode.com/problems/duplicate-zeros/

func duplicateZeros(arr []int) {
	zeros := 0
	for _, x := range arr {
		if x == 0 {
			zeros++
		}
	}
	n := len(arr)
	for i := n - 1; i >= 0; i-- {
		if i+zeros < n {
			arr[i+zeros] = arr[i]
		}
		if arr[i] == 0 {
			zeros--
			if i+zeros < n {
				arr[i+zeros] = 0
			}
		}
	}
}
