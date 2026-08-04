// LeetCode 1925 - Count Square Sum Triples
// https://leetcode.com/problems/count-square-sum-triples/

func countTriples(n int) int {
	squares := make(map[int]bool)
	for i := 1; i <= n; i++ {
		squares[i*i] = true
	}
	ans := 0
	for a := 1; a <= n; a++ {
		for b := 1; b <= n; b++ {
			if squares[a*a+b*b] {
				ans++
			}
		}
	}
	return ans
}
