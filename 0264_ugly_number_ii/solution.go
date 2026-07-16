// LeetCode 0264 - Ugly Number II
// https://leetcode.com/problems/ugly-number-ii/

func nthUglyNumber(n int) int {
	ugly := []int{1}
	index2, index3, index5 := 0, 0, 0
	for len(ugly) < n {
		nextUgly := min(ugly[index2]*2, ugly[index3]*3, ugly[index5]*5)
		ugly = append(ugly, nextUgly)
		if nextUgly == ugly[index2]*2 {
			index2++
		}
		if nextUgly == ugly[index3]*3 {
			index3++
		}
		if nextUgly == ugly[index5]*5 {
			index5++
		}
	}
	return ugly[len(ugly)-1]
}
