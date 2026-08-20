// LeetCode 0932 - Beautiful Array
// https://leetcode.com/problems/beautiful-array/

func beautifulArray(n int) []int {
	if n == 1 {
		return []int{1}
	}
	left := beautifulArray((n + 1) / 2)
	right := beautifulArray(n / 2)
	ans := make([]int, 0, n)
	for _, x := range left {
		ans = append(ans, 2*x-1)
	}
	for _, x := range right {
		ans = append(ans, 2*x)
	}
	return ans
}
