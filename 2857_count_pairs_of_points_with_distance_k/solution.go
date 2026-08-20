// LeetCode 2857 - Count Pairs of Points With Distance k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

func countPairs(coordinates [][]int, k int) int {
	freq := map[[2]int]int{}
	ans := 0
	for _, p := range coordinates {
		x, y := p[0], p[1]
		for a := 0; a <= k; a++ {
			b := k - a
			ans += freq[[2]int{x ^ a, y ^ b}]
		}
		freq[[2]int{x, y}]++
	}
	return ans
}
