// LeetCode 1491 - Average Salary Excluding the Minimum and Maximum Salary
// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

func average(salary []int) float64 {
	mn, mx, sum := salary[0], salary[0], 0
	for _, s := range salary {
		sum += s
		if s < mn {
			mn = s
		}
		if s > mx {
			mx = s
		}
	}
	return float64(sum-mn-mx) / float64(len(salary)-2)
}
