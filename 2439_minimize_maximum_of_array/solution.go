// LeetCode 2439 - Minimize Maximum of Array
// https://leetcode.com/problems/minimize-maximum-of-array/

func minimizeArrayValue(nums []int) int {
	var sum int64
	ans := 0
	for i, x := range nums {
		sum += int64(x)
		avg := int((sum + int64(i)) / int64(i+1))
		if avg > ans {
			ans = avg
		}
	}
	return ans
}
