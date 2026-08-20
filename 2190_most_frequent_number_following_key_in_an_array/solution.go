// LeetCode 2190 - Most Frequent Number Following Key In an Array
// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

func mostFrequent(nums []int, key int) int {
	freq := map[int]int{}
	best, ans := 0, 0
	for i := 0; i+1 < len(nums); i++ {
		if nums[i] == key {
			freq[nums[i+1]]++
			if freq[nums[i+1]] > best {
				best = freq[nums[i+1]]
				ans = nums[i+1]
			}
		}
	}
	return ans
}
