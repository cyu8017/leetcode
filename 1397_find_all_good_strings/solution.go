// LeetCode 1397 - Find All Good Strings
// https://leetcode.com/problems/find-all-good-strings/

func findGoodStrings(n int, s1 string, s2 string, evil string) int {
	const mod = 1000000007
	m := len(evil)
	pi := make([]int, m)
	for i := 1; i < m; i++ {
		j := pi[i-1]
		for j > 0 && evil[i] != evil[j] {
			j = pi[j-1]
		}
		if evil[i] == evil[j] {
			j++
		}
		pi[i] = j
	}
	trans := make([][26]int, m)
	for j := 0; j < m; j++ {
		for x := 0; x < 26; x++ {
			c := byte('a' + x)
			k := j
			for k > 0 && evil[k] != c {
				k = pi[k-1]
			}
			if evil[k] == c {
				k++
			}
			trans[j][x] = k
		}
	}
	type key struct {
		i, j    int
		lo, hi  bool
	}
	memo := map[key]int{}
	var dp func(i, j int, lo, hi bool) int
	dp = func(i, j int, lo, hi bool) int {
		if j == m {
			return 0
		}
		if i == n {
			return 1
		}
		k := key{i, j, lo, hi}
		if v, ok := memo[k]; ok {
			return v
		}
		a, b := 0, 25
		if lo {
			a = int(s1[i] - 'a')
		}
		if hi {
			b = int(s2[i] - 'a')
		}
		ans := 0
		for x := a; x <= b; x++ {
			ans = (ans + dp(i+1, trans[j][x], lo && x == a, hi && x == b)) % mod
		}
		memo[k] = ans
		return ans
	}
	return dp(0, 0, true, true)
}
