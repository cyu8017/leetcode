// LeetCode 1915 - Number of Wonderful Substrings
// https://leetcode.com/problems/number-of-wonderful-substrings/

func wonderfulSubstrings(word string) int64 {
	count := make([]int, 1024)
	count[0] = 1
	mask := 0
	var ans int64
	for i := 0; i < len(word); i++ {
		mask ^= 1 << (word[i] - 'a')
		ans += int64(count[mask])
		for bit := 0; bit < 10; bit++ {
			ans += int64(count[mask^(1<<bit)])
		}
		count[mask]++
	}
	return ans
}
