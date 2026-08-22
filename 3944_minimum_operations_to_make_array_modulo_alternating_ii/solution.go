// LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

func minOperations(nums []int, k int) int64 {
	evenFreq, oddFreq := make([]int64, k), make([]int64, k)
	for i, x := range nums {
		if i%2 == 0 {
			evenFreq[x%k]++
		} else {
			oddFreq[x%k]++
		}
	}
	costs := func(freq []int64) []int64 {
		double := make([]int64, 2*k)
		for i := 0; i < 2*k; i++ {
			double[i] = freq[i%k]
		}
		countPrefix, weightedPrefix := make([]int64, 2*k+1), make([]int64, 2*k+1)
		for i, x := range double {
			countPrefix[i+1] = countPrefix[i] + x
			weightedPrefix[i+1] = weightedPrefix[i] + int64(i)*x
		}
		rangeStats := func(l, r int) (int64, int64) {
			return countPrefix[r+1] - countPrefix[l],
				weightedPrefix[r+1] - weightedPrefix[l]
		}
		res := make([]int64, k)
		cw, cc := k/2, (k-1)/2
		for t := 0; t < k; t++ {
			cnt, sum := rangeStats(t, t+cw)
			res[t] += sum - int64(t)*cnt
			if cc > 0 {
				cnt, sum = rangeStats(t+k-cc, t+k-1)
				res[t] += int64(t+k)*cnt - sum
			}
		}
		return res
	}
	evenCost, oddCost := costs(evenFreq), costs(oddFreq)
	best1, best2, bestIndex := int64(1<<62), int64(1<<62), -1
	for i, x := range oddCost {
		if x < best1 {
			best2, best1, bestIndex = best1, x, i
		} else if x < best2 {
			best2 = x
		}
	}
	ans := int64(1 << 62)
	for x, cost := range evenCost {
		other := best1
		if x == bestIndex {
			other = best2
		}
		if cost+other < ans {
			ans = cost + other
		}
	}
	return ans
}