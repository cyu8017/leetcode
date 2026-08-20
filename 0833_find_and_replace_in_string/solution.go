// LeetCode 0833 - Find And Replace in String
// https://leetcode.com/problems/find-and-replace-in-string/

func findReplaceString(s string, indices []int, sources []string, targets []string) string {
	type rep struct {
		length int
		target string
	}
	replace := map[int]rep{}
	for i := range indices {
		idx, src, tgt := indices[i], sources[i], targets[i]
		if idx+len(src) <= len(s) && s[idx:idx+len(src)] == src {
			replace[idx] = rep{len(src), tgt}
		}
	}
	out := []byte{}
	i := 0
	for i < len(s) {
		if v, ok := replace[i]; ok {
			out = append(out, v.target...)
			i += v.length
		} else {
			out = append(out, s[i])
			i++
		}
	}
	return string(out)
}
