// LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

type subarrayState3957 struct {
	value int64
	count int
}

func maxSum(nums []int, m int, l int, r int) int64 {
	n := len(nums)
	prefix := make([]int64, n+1)
	for i, value := range nums {
		prefix[i+1] = prefix[i] + int64(value)
	}
	better := func(a, b subarrayState3957) bool {
		return a.value > b.value || a.value == b.value && a.count > b.count
	}
	run := func(penalty int64) subarrayState3957 {
		dp := make([]subarrayState3957, n+1)
		deque := make([]int, 0, n+1)
		candidateBetter := func(a, b int) bool {
			left := subarrayState3957{dp[a].value - prefix[a], dp[a].count}
			right := subarrayState3957{dp[b].value - prefix[b], dp[b].count}
			return better(left, right)
		}
		for end := 1; end <= n; end++ {
			addIndex := end - l
			if addIndex >= 0 {
				for len(deque) > 0 && candidateBetter(addIndex, deque[len(deque)-1]) {
					deque = deque[:len(deque)-1]
				}
				deque = append(deque, addIndex)
			}
			minIndex := end - r
			for len(deque) > 0 && deque[0] < minIndex {
				deque = deque[1:]
			}
			dp[end] = dp[end-1]
			if len(deque) > 0 {
				start := deque[0]
				take := subarrayState3957{
					dp[start].value + prefix[end] - prefix[start] - penalty,
					dp[start].count + 1,
				}
				if better(take, dp[end]) {
					dp[end] = take
				}
			}
		}
		return dp[n]
	}
	unconstrained := run(0)
	if unconstrained.count > 0 && unconstrained.count <= m {
		return unconstrained.value
	}
	if unconstrained.count > m {
		bound := int64(0)
		for _, value := range nums {
			if value >= 0 {
				bound += int64(value)
			} else {
				bound -= int64(value)
			}
		}
		low, high := int64(0), bound+1
		for low < high {
			mid := low + (high-low+1)/2
			if run(mid).count >= m {
				low = mid
			} else {
				high = mid - 1
			}
		}
		state := run(low)
		return state.value + low*int64(m)
	}
	const infinity int64 = 1 << 60
	bestSingle := -infinity
	deque := make([]int, 0, n+1)
	for end := 1; end <= n; end++ {
		addIndex := end - l
		if addIndex >= 0 {
			for len(deque) > 0 && prefix[deque[len(deque)-1]] >= prefix[addIndex] {
				deque = deque[:len(deque)-1]
			}
			deque = append(deque, addIndex)
		}
		minIndex := end - r
		for len(deque) > 0 && deque[0] < minIndex {
			deque = deque[1:]
		}
		if len(deque) > 0 {
			sum := prefix[end] - prefix[deque[0]]
			if sum > bestSingle {
				bestSingle = sum
			}
		}
	}
	return bestSingle
}