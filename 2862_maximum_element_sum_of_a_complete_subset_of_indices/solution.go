// LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

func maximumSum(nums []int) int64 {
	n := len(nums)
	var ans int64
	for i := 1; i <= n; i++ {
		var sum int64
		for j := i; j <= n; j += i {
			// j/i should be perfect square for complete subset starting? 
			// Actually: indices with same square-free part
			_ = j
		}
		_ = sum
	}
	groups := map[int]int64{}
	squareFree := func(x int) int {
		res := 1
		for p := 2; p*p <= x; p++ {
			cnt := 0
			for x%p == 0 {
				x /= p
				cnt++
			}
			if cnt%2 == 1 {
				res *= p
			}
		}
		if x > 1 {
			res *= x
		}
		return res
	}
	for i := 1; i <= n; i++ {
		sf := squareFree(i)
		groups[sf] += int64(nums[i-1])
		if groups[sf] > ans {
			ans = groups[sf]
		}
	}
	return ans
}
