// LeetCode 2451 - Odd String Difference
// https://leetcode.com/problems/odd-string-difference/

func oddString(words []string) string {
	diff := func(w string) string {
		b := make([]byte, 0, (len(w)-1)*4)
		for i := 1; i < len(w); i++ {
			d := int(w[i]) - int(w[i-1])
			b = append(b, byte(d+128), ',')
		}
		return string(b)
	}
	d0, d1 := diff(words[0]), diff(words[1])
	if d0 == d1 {
		for i := 2; i < len(words); i++ {
			if diff(words[i]) != d0 {
				return words[i]
			}
		}
	}
	if diff(words[2]) == d0 {
		return words[1]
	}
	return words[0]
}
