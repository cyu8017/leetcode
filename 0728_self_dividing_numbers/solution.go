// LeetCode 0728 - Self Dividing Numbers
// https://leetcode.com/problems/self-dividing-numbers/

func selfDividingNumbers(left int, right int) []int {
	isSelfDividing := func(num int) bool {
		x := num
		for x > 0 {
			digit := x % 10
			if digit == 0 || num%digit != 0 {
				return false
			}
			x /= 10
		}
		return true
	}
	result := []int{}
	for num := left; num <= right; num++ {
		if isSelfDividing(num) {
			result = append(result, num)
		}
	}
	return result
}
