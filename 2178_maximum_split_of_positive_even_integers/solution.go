// LeetCode 2178 - Maximum Split of Positive Even Integers
// https://leetcode.com/problems/maximum-split-of-positive-even-integers/

func maximumEvenSplit(finalSum int64) []int64 {
	if finalSum%2 != 0 {
		return []int64{}
	}
	ans := []int64{}
	for x := int64(2); x <= finalSum; x += 2 {
		ans = append(ans, x)
		finalSum -= x
	}
	ans[len(ans)-1] += finalSum
	return ans
}
