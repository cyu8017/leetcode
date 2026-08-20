// LeetCode 0985 - Sum of Even Numbers After Queries
// https://leetcode.com/problems/sum-of-even-numbers-after-queries/

func sumEvenAfterQueries(nums []int, queries [][]int) []int {
	even := 0
	for _, x := range nums {
		if x%2 == 0 {
			even += x
		}
	}
	ans := make([]int, len(queries))
	for qi, q := range queries {
		val, i := q[0], q[1]
		if nums[i]%2 == 0 {
			even -= nums[i]
		}
		nums[i] += val
		if nums[i]%2 == 0 {
			even += nums[i]
		}
		ans[qi] = even
	}
	return ans
}
