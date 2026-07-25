// LeetCode 1679 - Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

func maxOperations(nums []int, k int) int {
	c := map[int]int{}
	ans := 0
	for _, x := range nums {
		if c[k-x] > 0 {
			c[k-x]--
			ans++
		} else {
			c[x]++
		}
	}
	return ans
}
