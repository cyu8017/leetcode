// LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
// https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

func minimumOperationsToMakeEqual(x int, y int) int {
	if x <= y {
		return y - x
	}
	type item struct{ v, d int }
	q := []item{{x, 0}}
	seen := map[int]bool{x: true}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur.v == y {
			return cur.d
		}
		cands := []int{cur.v + 1, cur.v - 1}
		if cur.v%11 == 0 {
			cands = append(cands, cur.v/11)
		}
		if cur.v%5 == 0 {
			cands = append(cands, cur.v/5)
		}
		for _, nxt := range cands {
			if nxt > 0 && nxt < 2*x+20 && !seen[nxt] {
				seen[nxt] = true
				q = append(q, item{nxt, cur.d + 1})
			}
		}
	}
	return -1
}
