// LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

func maxProduct(nums []int, k int, limit int) int {
	const MIN = -5000
	sumAll := 0
	for _, v := range nums {
		sumAll += v
	}
	if abs(k) > sumAll {
		return -1
	}
	type key struct {
		i, product, state, kk int
	}
	memo := map[key]int{}
	var dp func(i, product, state, kk int) int
	dp = func(i, product, state, kk int) int {
		if i == len(nums) {
			if kk == 0 && state != 0 && product <= limit {
				return product
			}
			return MIN
		}
		kkkey := key{i, product, state, kk}
		if v, ok := memo[kkkey]; ok {
			return v
		}
		res := dp(i+1, product, state, kk)
		if state == 0 {
			res = max(res, dp(i+1, nums[i], 1, kk-nums[i]))
		}
		if state == 1 {
			np := product * nums[i]
			if np > limit+1 {
				np = limit + 1
			}
			res = max(res, dp(i+1, np, 2, kk+nums[i]))
		}
		if state == 2 {
			np := product * nums[i]
			if np > limit+1 {
				np = limit + 1
			}
			res = max(res, dp(i+1, np, 1, kk-nums[i]))
		}
		memo[kkkey] = res
		return res
	}
	ans := dp(0, 1, 0, k)
	if ans == MIN {
		return -1
	}
	return ans
}
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
