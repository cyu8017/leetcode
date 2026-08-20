// LeetCode 3139 - Minimum Cost to Equalize Array
// https://leetcode.com/problems/minimum-cost-to-equalize-array/

func minCostToEqualizeArray(nums []int, cost1 int, cost2 int) int {
	const mod = 1_000_000_007
	n := len(nums)
	minNum, maxNum := nums[0], nums[0]
	var sum int64
	for _, v := range nums {
		if v < minNum {
			minNum = v
		}
		if v > maxNum {
			maxNum = v
		}
		sum += int64(v)
	}
	if cost1*2 <= cost2 || n < 3 {
		totalGap := int64(maxNum)*int64(n) - sum
		return int(int64(cost1) * totalGap % mod)
	}
	ans := int64(1<<63 - 1)
	for target := maxNum; target < 2*maxNum; target++ {
		maxGap := target - minNum
		totalGap := int64(target)*int64(n) - sum
		pairs := totalGap / 2
		if alt := totalGap - int64(maxGap); alt < pairs {
			pairs = alt
		}
		cost := int64(cost1)*(totalGap-2*pairs) + int64(cost2)*pairs
		if cost < ans {
			ans = cost
		}
	}
	return int(ans % mod)
}
