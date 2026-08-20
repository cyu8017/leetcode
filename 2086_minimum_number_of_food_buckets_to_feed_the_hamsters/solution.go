// LeetCode 2086 - Minimum Number of Food Buckets to Feed the Hamsters
// https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

func minimumBuckets(hamsters string) int {
	b := []byte(hamsters)
	ans := 0
	for i := 0; i < len(b); i++ {
		if b[i] != 'H' {
			continue
		}
		if i > 0 && b[i-1] == 'B' {
			continue
		}
		if i+1 < len(b) && b[i+1] == '.' {
			b[i+1] = 'B'
			ans++
		} else if i > 0 && b[i-1] == '.' {
			b[i-1] = 'B'
			ans++
		} else {
			return -1
		}
	}
	return ans
}
