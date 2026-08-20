// LeetCode 3016 - Minimum Number of Pushes to Type Word II
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

func minimumPushes(word string) (ans int) {
	cnt := make([]int, 26)
	for _, c := range word {
		cnt[c-'a']++
	}
	sort.Ints(cnt)
	for i := 0; i < 26; i++ {
		ans += (i/8 + 1) * cnt[26-i-1]
	}
	return
}
