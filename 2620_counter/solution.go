// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/


func createCounter(n int) func() int {
	cur := n
	return func() int {
		v := cur
		cur++
		return v
	}
}
