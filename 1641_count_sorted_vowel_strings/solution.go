// LeetCode 1641 - Count Sorted Vowel Strings
// https://leetcode.com/problems/count-sorted-vowel-strings/

func countVowelStrings(n int) int {
	return comb1641(n+4, 4)
}

func comb1641(n, r int) int {
	if r > n-r {
		r = n - r
	}
	res := 1
	for i := 0; i < r; i++ {
		res = res * (n - i) / (i + 1)
	}
	return res
}
