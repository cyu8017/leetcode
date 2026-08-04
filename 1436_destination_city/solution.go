// LeetCode 1436 - Destination City
// https://leetcode.com/problems/destination-city/

func destCity(paths [][]string) string {
	starts := map[string]bool{}
	for _, p := range paths {
		starts[p[0]] = true
	}
	for _, p := range paths {
		if !starts[p[1]] {
			return p[1]
		}
	}
	return ""
}
