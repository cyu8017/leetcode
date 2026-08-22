// LeetCode 3481 - Apply Substitutions
// https://leetcode.com/problems/apply-substitutions/

func applySubstitutions(replacements [][]string, text string) string {
	mp := map[string]string{}
	for _, r := range replacements {
		mp[r[0]] = r[1]
	}
	var resolve func(string) string
	resolve = func(s string) string {
		out := []byte{}
		for i := 0; i < len(s); {
			if s[i] == '%' {
				j := i + 1
				for j < len(s) && s[j] != '%' {
					j++
				}
				key := s[i+1 : j]
				val := mp[key]
				out = append(out, resolve(val)...)
				i = j + 1
			} else {
				out = append(out, s[i])
				i++
			}
		}
		return string(out)
	}
	return resolve(text)
}
