// LeetCode 2516 - Take K of Each Character From Left and Right
// https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

func takeCharacters(s string, k int) int {
	n := len(s)
	cnt := [3]int{}
	for i := 0; i < n; i++ {
		cnt[s[i]-'a']++
	}
	if cnt[0] < k || cnt[1] < k || cnt[2] < k {
		return -1
	}
	need := [3]int{cnt[0] - k, cnt[1] - k, cnt[2] - k}
	window := [3]int{}
	left := 0
	maxMid := 0
	for right := 0; right < n; right++ {
		window[s[right]-'a']++
		for window[0] > need[0] || window[1] > need[1] || window[2] > need[2] {
			window[s[left]-'a']--
			left++
		}
		if right-left+1 > maxMid {
			maxMid = right - left + 1
		}
	}
	return n - maxMid
}
