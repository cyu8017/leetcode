// LeetCode 1647 - Minimum Deletions to Make Character Frequencies Unique
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

func minDeletions(s string) int {
	freq := [26]int{}
	for i := 0; i < len(s); i++ {
		freq[s[i]-'a']++
	}
	used := map[int]bool{}
	ans := 0
	for _, x := range freq {
		for x > 0 && used[x] {
			x--
			ans++
		}
		if x > 0 {
			used[x] = true
		}
	}
	return ans
}
