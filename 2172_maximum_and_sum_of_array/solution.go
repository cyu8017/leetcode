// LeetCode 2172 - Maximum AND Sum of Array
// https://leetcode.com/problems/maximum-and-sum-of-array/

func maximumANDSum(nums []int, numSlots int) int {
	n := len(nums)
	slots := numSlots
	maxMask := 1
	for i := 0; i < slots; i++ {
		maxMask *= 3
	}
	dp := make([]int, maxMask)
	for mask := 0; mask < maxMask; mask++ {
		cnt := 0
		x := mask
		for x > 0 {
			cnt += x % 3
			x /= 3
		}
		if cnt >= n {
			continue
		}
		v := nums[cnt]
		base := 1
		for s := 1; s <= slots; s++ {
			occ := (mask / base) % 3
			if occ < 2 {
				nm := mask + base
				cand := dp[mask] + (v & s)
				if cand > dp[nm] {
					dp[nm] = cand
				}
			}
			base *= 3
		}
	}
	ans := 0
	for _, v := range dp {
		if v > ans {
			ans = v
		}
	}
	return ans
}
