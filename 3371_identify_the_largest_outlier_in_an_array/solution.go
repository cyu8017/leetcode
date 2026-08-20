// LeetCode 3371 - Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

func getLargestOutlier(nums []int) int {
	sum := 0
	freq := map[int]int{}
	for _, x := range nums {
		sum += x
		freq[x]++
	}
	ans := int(-1e18)
	for _, x := range nums {
		// x as outlier => sum - x = 2 * specialSumCandidate? 
		// total = specialSum + sumElement + outlier
		// sumElement = specialSum => total = 2*specialSum + outlier => specialSum = (total-outlier)/2
		freq[x]--
		rem := sum - x
		if rem%2 == 0 {
			cand := rem / 2
			if freq[cand] > 0 && x > ans {
				ans = x
			}
		}
		freq[x]++
	}
	return ans
}
