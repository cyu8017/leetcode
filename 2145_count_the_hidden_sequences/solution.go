// LeetCode 2145 - Count the Hidden Sequences
// https://leetcode.com/problems/count-the-hidden-sequences/

func numberOfArrays(differences []int, lower int, upper int) int {
	var cur, mn, mx int64
	for _, d := range differences {
		cur += int64(d)
		if cur < mn {
			mn = cur
		}
		if cur > mx {
			mx = cur
		}
	}
	res := int(int64(upper-lower) - (mx - mn) + 1)
	if res < 0 {
		return 0
	}
	return res
}
