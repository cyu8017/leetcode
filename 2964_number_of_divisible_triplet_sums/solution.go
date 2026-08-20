// LeetCode 2964 - Number of Divisible Triplet Sums
// https://leetcode.com/problems/number-of-divisible-triplet-sums/

func divisibleTripletCount(nums []int, d int) int {
	n := len(nums)
	ans := 0
	for i := 0; i < n; i++ {
		freq := map[int]int{}
		for j := i + 1; j < n; j++ {
			need := (d - (nums[i]+nums[j])%d) % d
			ans += freq[need]
			freq[nums[j]%d]++
		}
	}
	return ans
}
