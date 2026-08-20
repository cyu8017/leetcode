// LeetCode 2804 - Array Prototype ForEach
// https://leetcode.com/problems/array-prototype-foreach/

func forEach(arr []int, callback func(int, int, []int), context interface{}) {
	for i, v := range arr {
		callback(v, i, arr)
	}
}
