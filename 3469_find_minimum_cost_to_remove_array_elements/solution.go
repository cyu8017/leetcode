// LeetCode 3469 - Find Minimum Cost to Remove Array Elements
// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

func minCost(nums []int) int {
	n := len(nums)
	memo := map[[2]int]int{}
	var dfs func(i, prev int) int
	dfs = func(i, prev int) int {
		if i >= n {
			if prev == -1 {
				return 0
			}
			return nums[prev]
		}
		key := [2]int{i, prev}
		if v, ok := memo[key]; ok {
			return v
		}
		var res int
		if prev == -1 {
			if i+1 >= n {
				res = nums[i]
			} else if i+2 >= n {
				res = max2(nums[i], nums[i+1])
			} else {
				a, b, c := nums[i], nums[i+1], nums[i+2]
				res = min3(
					max2(b, c)+dfs(i+3, i),
					max2(a, c)+dfs(i+3, i+1),
					max2(a, b)+dfs(i+3, i+2),
				)
			}
		} else {
			if i+1 >= n {
				res = max2(nums[prev], nums[i])
			} else {
				a, b, c := nums[prev], nums[i], nums[i+1]
				res = min3(
					max2(b, c)+dfs(i+2, prev),
					max2(a, c)+dfs(i+2, i),
					max2(a, b)+dfs(i+2, i+1),
				)
			}
		}
		memo[key] = res
		return res
	}
	return dfs(0, -1)
}

func min3(a, b, c int) int {
	if a > b {
		a = b
	}
	if a > c {
		a = c
	}
	return a
}
func max2(a, b int) int {
	if a > b {
		return a
	}
	return b
}
