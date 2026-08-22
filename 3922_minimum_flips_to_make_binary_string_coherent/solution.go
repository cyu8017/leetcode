// LeetCode 3922 - Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

func minFlips(s string) int {
	ones := 0
	for i := range s {
		if s[i] == '1' {
			ones++
		}
	}
	answer := ones
	if ones > 0 {
		answer = ones - 1
	}
	zeros := len(s) - ones
	if zeros < answer {
		answer = zeros
	}
	if len(s) >= 2 {
		cost := 0
		for i := range s {
			want := byte('0')
			if i == 0 || i == len(s)-1 {
				want = '1'
			}
			if s[i] != want {
				cost++
			}
		}
		if cost < answer {
			answer = cost
		}
	}
	return answer
}