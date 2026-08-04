// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

func maxNumberOfBalloons(text string) int {
	count := [26]int{}
	for i := 0; i < len(text); i++ {
		count[text[i]-'a']++
	}
	ans := count['b'-'a']
	for _, v := range []int{count['a'-'a'], count['l'-'a'] / 2, count['o'-'a'] / 2, count['n'-'a']} {
		if v < ans {
			ans = v
		}
	}
	return ans
}
