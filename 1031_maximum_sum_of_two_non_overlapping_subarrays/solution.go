// LeetCode 1031 - Maximum Sum of Two Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

func maxSumTwoNoOverlap(nums []int, firstLen, secondLen int) int {
	prefix := make([]int, len(nums)+1)
	for i, x := range nums {
		prefix[i+1] = prefix[i] + x
	}
	best := func(a, b int) int {
		bestA, ans := 0, 0
		for i := a + b; i < len(prefix); i++ {
			if v := prefix[i-b] - prefix[i-b-a]; v > bestA {
				bestA = v
			}
			if v := bestA + prefix[i] - prefix[i-b]; v > ans {
				ans = v
			}
		}
		return ans
	}
	x, y := best(firstLen, secondLen), best(secondLen, firstLen)
	if x > y {
		return x
	}
	return y
}
