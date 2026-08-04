// LeetCode 1497 - Check If Array Pairs Are Divisible by k
// https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

func canArrange(arr []int, k int) bool {
	count := make([]int, k)
	for _, x := range arr {
		r := x % k
		if r < 0 {
			r += k
		}
		count[r]++
	}
	if count[0]%2 != 0 {
		return false
	}
	if k%2 == 0 && count[k/2]%2 != 0 {
		return false
	}
	for r := 1; r < (k+1)/2; r++ {
		if count[r] != count[k-r] {
			return false
		}
	}
	return true
}
