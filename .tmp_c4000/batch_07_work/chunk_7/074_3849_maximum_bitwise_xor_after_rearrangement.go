// LeetCode 3849 - Maximum Bitwise Xor After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

func maximumXor(s string, t string) string {
	cnt := make([]int, 2)
	for _, c := range t {
		cnt[c-'0']++
	}

	ans := make([]byte, len(s))
	for i := 0; i < len(s); i++ {
		x := s[i] - '0'
		if cnt[x^1] > 0 {
			cnt[x^1]--
			ans[i] = '1'
		} else {
			cnt[x]--
			ans[i] = '0'
		}
	}

	return string(ans)
}
