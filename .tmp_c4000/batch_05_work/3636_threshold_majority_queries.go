// LeetCode 3636 - Threshold Majority Queries
// https://leetcode.com/problems/threshold-majority-queries/

func subarrayMajority(nums []int, queries [][]int) []int {
	ans := make([]int, len(queries))
	for qi, q := range queries {
		l, r, thresh := q[0], q[1], q[2]
		freq := map[int]int{}
		for i := l; i <= r; i++ {
			freq[nums[i]]++
		}
		bestVal, bestCnt := -1, 0
		for v, c := range freq {
			if c >= thresh && (c > bestCnt || (c == bestCnt && (bestVal == -1 || v < bestVal))) {
				bestCnt = c
				bestVal = v
			}
		}
		ans[qi] = bestVal
	}
	return ans
}
