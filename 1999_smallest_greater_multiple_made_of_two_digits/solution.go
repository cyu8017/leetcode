// LeetCode 1999 - Smallest Greater Multiple Made of Two Digits
// https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits/

func findInteger(k int, digit1 int, digit2 int) int {
	digitSet := map[int]bool{digit1: true, digit2: true}
	digits := []int{}
	for d := 0; d <= 9; d++ {
		if digitSet[d] {
			digits = append(digits, d)
		}
	}
	q := []int{}
	seen := make(map[int]bool)
	for _, d := range digits {
		if d != 0 {
			q = append(q, d)
			seen[d] = true
		}
	}
	if len(q) == 0 {
		return -1
	}
	const maxInt = 1<<31 - 1
	for len(q) > 0 {
		x := q[0]
		q = q[1:]
		if x > k && x%k == 0 {
			return x
		}
		for _, d := range digits {
			nx := x*10 + d
			if nx <= maxInt && !seen[nx] {
				seen[nx] = true
				q = append(q, nx)
			}
		}
	}
	return -1
}
