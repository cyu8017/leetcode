// LeetCode 0249 - Group Shifted Strings
// https://leetcode.com/problems/group-shifted-strings/

func groupStrings(strings []string) [][]string {
	groups := make(map[string][]string)
	order := make([]string, 0)

	for _, text := range strings {
		var key string
		if text == "" {
			key = ""
		} else {
			base := int(text[0])
			shifts := make([]byte, len(text))
			for index := 0; index < len(text); index++ {
				shifts[index] = byte((int(text[index])-base+26)%26) + '0'
			}
			key = string(shifts)
		}
		if _, ok := groups[key]; !ok {
			order = append(order, key)
		}
		groups[key] = append(groups[key], text)
	}

	result := make([][]string, 0, len(order))
	for _, key := range order {
		result = append(result, groups[key])
	}
	return result
}
