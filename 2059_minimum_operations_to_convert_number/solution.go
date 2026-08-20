// LeetCode 2059 - Minimum Operations to Convert Number
// https://leetcode.com/problems/minimum-operations-to-convert-number/

func minimumOperations(nums []int, start int, goal int) int {
	if start == goal {
		return 0
	}
	vis := map[int]bool{start: true}
	q := []int{start}
	steps := 0
	for len(q) > 0 {
		steps++
		sz := len(q)
		for i := 0; i < sz; i++ {
			cur := q[0]
			q = q[1:]
			for _, x := range nums {
				for _, nxt := range []int{cur + x, cur - x, cur ^ x} {
					if nxt == goal {
						return steps
					}
					if nxt >= 0 && nxt <= 1000 && !vis[nxt] {
						vis[nxt] = true
						q = append(q, nxt)
					}
				}
			}
		}
	}
	return -1
}
