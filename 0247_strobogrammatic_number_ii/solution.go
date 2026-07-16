// LeetCode 0247 - Strobogrammatic Number II
// https://leetcode.com/problems/strobogrammatic-number-ii/

func findStrobogrammatic(n int) []string {
	pairs := [][2]string{
		{"0", "0"},
		{"1", "1"},
		{"6", "9"},
		{"8", "8"},
		{"9", "6"},
	}

	var build func(left, right int) []string
	build = func(left, right int) []string {
		if left > right {
			return []string{""}
		}
		if left == right {
			return []string{"0", "1", "8"}
		}
		result := make([]string, 0)
		for _, pair := range pairs {
			start, end := pair[0], pair[1]
			if left == 0 && start == "0" {
				continue
			}
			for _, middle := range build(left+1, right-1) {
				result = append(result, start+middle+end)
			}
		}
		return result
	}

	return build(0, n-1)
}
