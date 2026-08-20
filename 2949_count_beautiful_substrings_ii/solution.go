// LeetCode 2949 - Count Beautiful Substrings II
// https://leetcode.com/problems/count-beautiful-substrings-ii/

func beautifulSubstrings(s string, k int) int64 {
	isVowel := func(c byte) bool {
		return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
	}
	// find minimal x such that x*x % k == 0
	x := 1
	for (x*x)%k != 0 {
		x++
	}
	type key struct{ bal, mod int }
	freq := map[key]int{{0, 0}: 1}
	bal := 0
	var ans int64
	vowels := 0
	for i := 0; i < len(s); i++ {
		if isVowel(s[i]) {
			bal++
			vowels++
		} else {
			bal--
		}
		kk := key{bal, vowels % x}
		ans += int64(freq[kk])
		freq[kk]++
	}
	return ans
}
