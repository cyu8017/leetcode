// LeetCode 1138 - Alphabet Board Path
// https://leetcode.com/problems/alphabet-board-path/

func alphabetBoardPath(target string) string {
	r, c := 0, 0
	out := []byte{}
	for i := 0; i < len(target); i++ {
		tr := int(target[i]-'a') / 5
		tc := int(target[i]-'a') % 5
		for r > tr {
			out = append(out, 'U')
			r--
		}
		for c > tc {
			out = append(out, 'L')
			c--
		}
		for c < tc {
			out = append(out, 'R')
			c++
		}
		for r < tr {
			out = append(out, 'D')
			r++
		}
		out = append(out, '!')
	}
	return string(out)
}
