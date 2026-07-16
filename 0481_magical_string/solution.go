// LeetCode 0481 - Magical String
// https://leetcode.com/problems/magical-string/

func magicalString(n int) int {
	if n == 0 {
		return 0
	}
	seq := []int{1, 2, 2}
	index := 2
	for len(seq) < n {
		if seq[index] == 1 {
			if seq[len(seq)-1] == 2 {
				seq = append(seq, 1)
			} else {
				seq = append(seq, 2)
			}
		} else {
			value := 1
			if seq[len(seq)-1] == 2 {
				value = 1
			} else {
				value = 2
			}
			seq = append(seq, value, value)
		}
		index++
	}
	ones := 0
	for i := 0; i < n; i++ {
		if seq[i] == 1 {
			ones++
		}
	}
	return ones
}
