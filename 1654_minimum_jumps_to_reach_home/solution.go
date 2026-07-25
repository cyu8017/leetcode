// LeetCode 1654 - Minimum Jumps to Reach Home
// https://leetcode.com/problems/minimum-jumps-to-reach-home/

func minimumJumps(forbidden []int, a, b, x int) int {
	bad := make(map[int]bool, len(forbidden))
	limit := x
	for _, f := range forbidden {
		bad[f] = true
		if f > limit {
			limit = f
		}
	}
	limit += a + b

	type state struct {
		pos  int
		back bool
	}
	type item struct {
		pos, dist int
		back      bool
	}
	q := []item{{0, 0, false}}
	seen := map[state]bool{{0, false}: true}

	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur.pos == x {
			return cur.dist
		}
		candidates := []struct {
			np   int
			back bool
		}{{cur.pos + a, false}}
		if !cur.back {
			candidates = append(candidates, struct {
				np   int
				back bool
			}{cur.pos - b, true})
		}
		for _, c := range candidates {
			if c.np < 0 || c.np > limit || bad[c.np] {
				continue
			}
			st := state{c.np, c.back}
			if seen[st] {
				continue
			}
			seen[st] = true
			q = append(q, item{c.np, cur.dist + 1, c.back})
		}
	}
	return -1
}
