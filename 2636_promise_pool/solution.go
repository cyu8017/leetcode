// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/


func promisePool(functions []func() int, n int) []int {
	ans := make([]int, len(functions))
	type job struct{ i int; fn func() int }
	jobs := make(chan job, len(functions))
	for i, fn := range functions {
		jobs <- job{i, fn}
	}
	close(jobs)
	done := make(chan struct{}, n)
	for w := 0; w < n; w++ {
		go func() {
			for j := range jobs {
				ans[j.i] = j.fn()
			}
			done <- struct{}{}
		}()
	}
	for w := 0; w < n; w++ {
		<-done
	}
	return ans
}
