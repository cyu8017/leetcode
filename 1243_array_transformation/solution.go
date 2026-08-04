// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

func transformArray(arr []int) []int {
	for {
		nxt := append([]int{}, arr...)
		changed := false
		for i := 1; i < len(arr)-1; i++ {
			if arr[i] < arr[i-1] && arr[i] < arr[i+1] {
				nxt[i]++
				changed = true
			} else if arr[i] > arr[i-1] && arr[i] > arr[i+1] {
				nxt[i]--
				changed = true
			}
		}
		if !changed {
			return arr
		}
		arr = nxt
	}
}
