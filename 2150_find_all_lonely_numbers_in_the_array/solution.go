// LeetCode 2150 - Find All Lonely Numbers in the Array
// https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

func findLonely(nums []int) []int {
	freq := map[int]int{}
	for _, x := range nums {
		freq[x]++
	}
	ans := []int{}
	for x, c := range freq {
		if c == 1 && freq[x-1] == 0 && freq[x+1] == 0 {
			ans = append(ans, x)
		}
	}
	return ans
}
