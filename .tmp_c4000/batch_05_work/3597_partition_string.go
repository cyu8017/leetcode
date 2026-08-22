// LeetCode 3597 - Partition String 
// https://leetcode.com/problems/partition-string/

func partitionString(s string) (ans []string) {
	vis := make(map[string]bool)
	t := ""
	for _, c := range s {
		t += string(c)
		if !vis[t] {
			vis[t] = true
			ans = append(ans, t)
			t = ""
		}
	}
	return
}
