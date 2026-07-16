// LeetCode 0093 - Restore IP Addresses
// https://leetcode.com/problems/restore-ip-addresses/

func restoreIpAddresses(s string) []string {
	result := []string{}
	path := []string{}

	var backtrack func(start int)
	backtrack = func(start int) {
		if len(path) == 4 {
			if start == len(s) {
				result = append(result, path[0]+"."+path[1]+"."+path[2]+"."+path[3])
			}
			return
		}

		for length := 1; length <= 3; length++ {
			if start+length > len(s) {
				break
			}
			part := s[start : start+length]
			if (part[0] == '0' && len(part) > 1) || toInt(part) > 255 {
				continue
			}
			path = append(path, part)
			backtrack(start + length)
			path = path[:len(path)-1]
		}
	}

	backtrack(0)
	return result
}

func toInt(part string) int {
	value := 0
	for i := 0; i < len(part); i++ {
		value = value*10 + int(part[i]-'0')
	}
	return value
}
