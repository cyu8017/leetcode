// LeetCode 3340 - Check Balanced String
// https://leetcode.com/problems/check-balanced-string/

func isBalanced(num string) bool {
	even, odd := 0, 0
	for i, c := range num {
		if i%2 == 0 {
			even += int(c - '0')
		} else {
			odd += int(c - '0')
		}
	}
	return even == odd
}
