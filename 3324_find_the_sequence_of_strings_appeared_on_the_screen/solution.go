// LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
// https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

func stringSequence(target string) []string {
	ans := []string{}
	cur := []byte{}
	for _, ch := range target {
		cur = append(cur, 'a')
		ans = append(ans, string(cur))
		for cur[len(cur)-1] != byte(ch) {
			cur[len(cur)-1]++
			ans = append(ans, string(cur))
		}
	}
	return ans
}
