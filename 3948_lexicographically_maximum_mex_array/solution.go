// LeetCode 3948 - Lexicographically Maximum MEX Array
// https://leetcode.com/problems/lexicographically-maximum-mex-array/

func maxMexArray(nums []int) []int {
	n := len(nums)
	remaining := make([]int, n+2)
	for _, x := range nums {
		if x <= n+1 {
			remaining[x]++
		}
	}
	mex := 0
	for remaining[mex] > 0 {
		mex++
	}
	answer := make([]int, 0)
	seen := make([]int, n+2)
	stamp, index := 0, 0
	for index < n {
		if mex == 0 {
			answer = append(answer, 0)
			x := nums[index]
			if x <= n+1 {
				remaining[x]--
			}
			index++
			continue
		}
		stamp++
		need := mex
		for need > 0 {
			x := nums[index]
			if x < mex && seen[x] != stamp {
				seen[x] = stamp
				need--
			}
			if x <= n+1 {
				remaining[x]--
			}
			index++
		}
		answer = append(answer, mex)
		mex = 0
		for remaining[mex] > 0 {
			mex++
		}
	}
	return answer
}