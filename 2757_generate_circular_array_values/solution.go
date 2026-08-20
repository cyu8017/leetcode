// LeetCode 2757 - Generate Circular Array Values
// https://leetcode.com/problems/generate-circular-array-values/

func cyclicGenerator(arr []int, startIndex int) func() int {
	i := startIndex
	n := len(arr)
	return func() int {
		v := arr[i]
		i = (i + 1) % n
		return v
	}
}
