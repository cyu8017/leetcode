// LeetCode 2798 - Number of Employees Who Met the Target
// https://leetcode.com/problems/number-of-employees-who-met-the-target/

func numberOfEmployeesWhoMetTarget(hours []int, target int) int {
	ans := 0
	for _, h := range hours {
		if h >= target {
			ans++
		}
	}
	return ans
}
