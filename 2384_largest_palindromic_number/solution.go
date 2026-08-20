// LeetCode 2384 - Largest Palindromic Number
// https://leetcode.com/problems/largest-palindromic-number/

func largestPalindromic(num string) string {
	cnt := [10]int{}
	for i := 0; i < len(num); i++ {
		cnt[num[i]-'0']++
	}
	left := []byte{}
	for d := 9; d >= 0; d-- {
		for cnt[d] >= 2 {
			if d == 0 && len(left) == 0 {
				break
			}
			left = append(left, byte('0'+d))
			cnt[d] -= 2
		}
	}
	mid := byte(0)
	for d := 9; d >= 0; d-- {
		if cnt[d] > 0 {
			mid = byte('0' + d)
			break
		}
	}
	if len(left) == 0 {
		if mid != 0 {
			return string([]byte{mid})
		}
		return "0"
	}
	right := make([]byte, len(left))
	for i := range left {
		right[len(left)-1-i] = left[i]
	}
	if mid != 0 {
		return string(left) + string([]byte{mid}) + string(right)
	}
	return string(left) + string(right)
}
