// LeetCode 2600 - K Items With the Maximum Sum
// https://leetcode.com/problems/k-items-with-the-maximum-sum/


func kItemsWithMaximumSum(numOnes int, numZeros int, numNegOnes int, k int) int {
	ans := 0
	take := numOnes
	if take > k {
		take = k
	}
	ans += take
	k -= take
	take = numZeros
	if take > k {
		take = k
	}
	k -= take
	take = numNegOnes
	if take > k {
		take = k
	}
	ans -= take
	return ans
}
