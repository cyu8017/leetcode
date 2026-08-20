// LeetCode 0989 - Add to Array-Form of Integer
// https://leetcode.com/problems/add-to-array-form-of-integer/

func addToArrayForm(num []int, k int) []int {
	i := len(num) - 1
	for k > 0 || i >= 0 {
		if i >= 0 {
			k += num[i]
			num[i] = k % 10
			i--
		} else {
			num = append([]int{k % 10}, num...)
		}
		k /= 10
	}
	return num
}
