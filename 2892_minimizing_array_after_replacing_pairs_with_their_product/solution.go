// LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
// https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

func minArrayLength(nums []int, k int) int {
	ans := 0
	prod := 1
	started := false
	for _, v := range nums {
		if !started {
			prod = v
			started = true
			ans = 1
			continue
		}
		if prod <= k/v || (prod*v <= k && v != 0) {
			if v == 0 {
				prod = 0
			} else if prod <= k/v {
				prod *= v
			} else {
				ans++
				prod = v
			}
		} else {
			ans++
			prod = v
		}
	}
	// simpler approach
	ans = 0
	i := 0
	n := len(nums)
	for i < n {
		prod := nums[i]
		j := i + 1
		for j < n {
			if nums[j] != 0 && prod > k/nums[j] {
				break
			}
			prod *= nums[j]
			if prod > k {
				break
			}
			j++
		}
		ans++
		i = j
		if i == n {
			break
		}
		// if couldn't merge any, still advance
		if j == i+0 {
		}
	}
	// clean rewrite
	ans = 1
	prod = nums[0]
	for i := 1; i < len(nums); i++ {
		if prod <= k && nums[i] <= k && (nums[i] == 0 || prod <= k/nums[i]) {
			prod *= nums[i]
		} else {
			ans++
			prod = nums[i]
		}
	}
	return ans
}
