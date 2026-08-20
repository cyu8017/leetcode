// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/


func promiseAll(functions []func() interface{}) []interface{} {
	ans := make([]interface{}, len(functions))
	done := make(chan int, len(functions))
	for i, fn := range functions {
		i, fn := i, fn
		go func() {
			ans[i] = fn()
			done <- i
		}()
	}
	for range functions {
		<-done
	}
	return ans
}
