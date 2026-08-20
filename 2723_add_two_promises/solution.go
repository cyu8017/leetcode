// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/


func addTwoPromises(promise1, promise2 func() int) int {
	return promise1() + promise2()
}
