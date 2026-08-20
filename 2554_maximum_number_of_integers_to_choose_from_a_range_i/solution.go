// LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/


func maxCount(banned []int, n int, maxSum int) int {
	ban := map[int]bool{}
	for _, x := range banned {
		ban[x] = true
	}
	ans, sum := 0, 0
	for i := 1; i <= n; i++ {
		if ban[i] {
			continue
		}
		if sum+i > maxSum {
			break
		}
		sum += i
		ans++
	}
	return ans
}
