// LeetCode 2899 - Last Visited Integers
// https://leetcode.com/problems/last-visited-integers/

func lastVisitedIntegers(nums []int) []int {
	seen := []int{}
	ans := []int{}
	k := 0
	for _, v := range nums {
		if v != -1 {
			seen = append(seen, v)
			k = 0
		} else {
			k++
			if k > len(seen) {
				ans = append(ans, -1)
			} else {
				ans = append(ans, seen[len(seen)-k])
			}
		}
	}
	return ans
}
