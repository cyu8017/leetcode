// LeetCode 0722 - Remove Comments
// https://leetcode.com/problems/remove-comments/

func removeComments(source []string) []string {
	result := []string{}
	buffer := []byte{}
	inBlock := false
	for _, line := range source {
		i := 0
		for i < len(line) {
			if inBlock {
				if i+1 < len(line) && line[i:i+2] == "*/" {
					inBlock = false
					i += 2
				} else {
					i++
				}
			} else if i+1 < len(line) && line[i:i+2] == "/*" {
				inBlock = true
				i += 2
			} else if i+1 < len(line) && line[i:i+2] == "//" {
				break
			} else {
				buffer = append(buffer, line[i])
				i++
			}
		}
		if !inBlock && len(buffer) > 0 {
			result = append(result, string(buffer))
			buffer = []byte{}
		}
	}
	return result
}
