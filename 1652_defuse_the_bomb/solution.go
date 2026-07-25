// LeetCode 1652 - Defuse the Bomb
// https://leetcode.com/problems/defuse-the-bomb/

func decrypt(code []int, k int) []int {
	n := len(code)
	ans := make([]int, n)
	if k == 0 {
		return ans
	}
	a := append(append([]int{}, code...), code...)
	for i := 0; i < n; i++ {
		if k > 0 {
			sum := 0
			for j := i + 1; j <= i+k; j++ {
				sum += a[j]
			}
			ans[i] = sum
		} else {
			sum := 0
			for j := i + n + k; j < i+n; j++ {
				sum += a[j]
			}
			ans[i] = sum
		}
	}
	return ans
}
