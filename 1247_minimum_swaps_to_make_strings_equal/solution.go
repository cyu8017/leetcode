// LeetCode 1247 - Minimum Swaps to Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

func minimumSwap(s1 string, s2 string) int {
	xy, yx := 0, 0
	for i := 0; i < len(s1); i++ {
		if s1[i] == 'x' && s2[i] == 'y' {
			xy++
		} else if s1[i] == 'y' && s2[i] == 'x' {
			yx++
		}
	}
	if (xy+yx)%2 != 0 {
		return -1
	}
	return xy/2 + yx/2 + 2*(xy%2)
}
