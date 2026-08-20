// LeetCode 0816 - Ambiguous Coordinates
// https://leetcode.com/problems/ambiguous-coordinates/

func ambiguousCoordinates(s string) []string {
	digits := s[1 : len(s)-1]
	candidates := func(frag string) []string {
		options := []string{}
		if frag == "" || (len(frag) > 1 && frag[0] == '0' && frag[len(frag)-1] == '0') {
			return options
		}
		if frag[0] == '0' && len(frag) > 1 {
			if frag[len(frag)-1] != '0' {
				return []string{"0." + frag[1:]}
			}
			return options
		}
		options = append(options, frag)
		if frag[len(frag)-1] == '0' {
			return options
		}
		for i := 1; i < len(frag); i++ {
			options = append(options, frag[:i]+"."+frag[i:])
		}
		return options
	}
	answer := []string{}
	for i := 1; i < len(digits); i++ {
		for _, left := range candidates(digits[:i]) {
			for _, right := range candidates(digits[i:]) {
				answer = append(answer, "("+left+", "+right+")")
			}
		}
	}
	return answer
}
