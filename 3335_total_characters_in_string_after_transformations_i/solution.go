// LeetCode 3335 - Total Characters in String After Transformations I
// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

func lengthAfterTransformations(s string, t int) int {
	const mod = 1000000007
	cnt := [26]int{}
	for _, c := range s {
		cnt[c-'a']++
	}
	for step := 0; step < t; step++ {
		ncnt := [26]int{}
		for i := 0; i < 25; i++ {
			ncnt[i+1] = (ncnt[i+1] + cnt[i]) % mod
		}
		ncnt[0] = (ncnt[0] + cnt[25]) % mod
		ncnt[1] = (ncnt[1] + cnt[25]) % mod
		cnt = ncnt
	}
	ans := 0
	for _, v := range cnt {
		ans = (ans + v) % mod
	}
	return ans
}
