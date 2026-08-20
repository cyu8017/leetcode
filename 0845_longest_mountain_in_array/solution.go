// LeetCode 0845 - Longest Mountain in Array
// https://leetcode.com/problems/longest-mountain-in-array/

func longestMountain(arr []int) int {
	n := len(arr)
	ans, i := 0, 0
	for i < n {
		j := i
		if j+1 < n && arr[j] < arr[j+1] {
			for j+1 < n && arr[j] < arr[j+1] {
				j++
			}
			if j+1 < n && arr[j] > arr[j+1] {
				for j+1 < n && arr[j] > arr[j+1] {
					j++
				}
				if j-i+1 > ans {
					ans = j - i + 1
				}
				i = j
				continue
			}
		}
		i++
	}
	return ans
}
