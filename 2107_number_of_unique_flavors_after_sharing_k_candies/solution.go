// LeetCode 2107 - Number of Unique Flavors After Sharing K Candies
// https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/

func shareCandies(candies []int, k int) int {
	n := len(candies)
	freq := map[int]int{}
	for _, c := range candies {
		freq[c]++
	}
	if k == 0 {
		return len(freq)
	}
	ans := 0
	for i := 0; i < k; i++ {
		freq[candies[i]]--
		if freq[candies[i]] == 0 {
			delete(freq, candies[i])
		}
	}
	ans = len(freq)
	for i := k; i < n; i++ {
		freq[candies[i-k]]++
		freq[candies[i]]--
		if freq[candies[i]] == 0 {
			delete(freq, candies[i])
		}
		if len(freq) > ans {
			ans = len(freq)
		}
	}
	return ans
}
