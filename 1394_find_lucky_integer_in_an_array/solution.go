// LeetCode 1394 - Find Lucky Integer in an Array
// https://leetcode.com/problems/find-lucky-integer-in-an-array/

func findLucky(arr []int) int {
	count := map[int]int{}
	for _, x := range arr {
		count[x]++
	}
	ans := -1
	for x, c := range count {
		if x == c && x > ans {
			ans = x
		}
	}
	return ans
}
