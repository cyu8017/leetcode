// LeetCode 2562 - Find the Array Concatenation Value
// https://leetcode.com/problems/find-the-array-concatenation-value/


func findTheArrayConcVal(nums []int) int64 {
	var ans int64
	l, r := 0, len(nums)-1
	for l <= r {
		if l == r {
			ans += int64(nums[l])
			break
		}
		left, right := nums[l], nums[r]
		pow := 1
		for t := right; t > 0; t /= 10 {
			pow *= 10
		}
		ans += int64(left)*int64(pow) + int64(right)
		l++
		r--
	}
	return ans
}
