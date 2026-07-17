// LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

func minFlips(s string) int {
	n := len(s)
	doubled := s + s
	alt0 := 0
	alt1 := 0

	expected := func(i int, even string) byte {
		if i%2 == 0 {
			return even[0]
		}
		return even[1]
	}

	for i := 0; i < n; i++ {
		if doubled[i] != expected(i, "01") {
			alt0++
		}
		if doubled[i] != expected(i, "10") {
			alt1++
		}
	}

	answer := alt0
	if alt1 < answer {
		answer = alt1
	}

	for i := 0; i < n; i++ {
		if doubled[i] != expected(i, "01") {
			alt0--
		}
		if doubled[i+n] != expected(i+n, "01") {
			alt0++
		}
		if doubled[i] != expected(i, "10") {
			alt1--
		}
		if doubled[i+n] != expected(i+n, "10") {
			alt1++
		}
		if alt0 < answer {
			answer = alt0
		}
		if alt1 < answer {
			answer = alt1
		}
	}
	return answer
}
