// LeetCode 2678 - Number of Senior Citizens
// https://leetcode.com/problems/number-of-senior-citizens/


func countSeniors(details []string) int {
	ans := 0
	for _, d := range details {
		age := int(d[11]-'0')*10 + int(d[12]-'0')
		if age > 60 {
			ans++
		}
	}
	return ans
}
