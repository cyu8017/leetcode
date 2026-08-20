// LeetCode 2898 - Maximum Linear Stock Score
// https://leetcode.com/problems/maximum-linear-stock-score/

func maxScore(prices []int) int64 {
	best := map[int]int64{}
	var ans int64
	for i, p := range prices {
		key := p - (i + 1)
		cand := best[key] + int64(p)
		if cand > best[key] {
			best[key] = cand
		}
		if best[key] > ans {
			ans = best[key]
		}
	}
	return ans
}
