// LeetCode 2237 - Count Positions on Street With Required Brightness
// https://leetcode.com/problems/count-positions-on-street-with-required-brightness/

func meetRequirement(n int, lights [][]int, requirement []int) int {
	diff := make([]int, n+1)
	for _, light := range lights {
		pos, r := light[0], light[1]
		l := pos - r
		if l < 0 {
			l = 0
		}
		rr := pos + r
		if rr >= n {
			rr = n - 1
		}
		diff[l]++
		diff[rr+1]--
	}
	ans, cur := 0, 0
	for i := 0; i < n; i++ {
		cur += diff[i]
		if cur >= requirement[i] {
			ans++
		}
	}
	return ans
}
