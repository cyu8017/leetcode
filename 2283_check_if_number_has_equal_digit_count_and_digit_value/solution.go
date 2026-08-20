// LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

func digitCount(num string) bool {
	cnt := make([]int, 10)
	for i := 0; i < len(num); i++ {
		cnt[num[i]-'0']++
	}
	for i := 0; i < len(num); i++ {
		if cnt[i] != int(num[i]-'0') {
			return false
		}
	}
	return true
}
