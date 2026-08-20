// LeetCode 0752 - Open the Lock
// https://leetcode.com/problems/open-the-lock/

func openLock(deadends []string, target string) int {
	dead := map[string]bool{}
	for _, d := range deadends {
		dead[d] = true
	}
	if dead["0000"] {
		return -1
	}
	type item struct {
		state string
		steps int
	}
	queue := []item{{"0000", 0}}
	seen := map[string]bool{"0000": true}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur.state == target {
			return cur.steps
		}
		b := []byte(cur.state)
		for i := 0; i < 4; i++ {
			orig := b[i]
			for _, delta := range []int{-1, 1} {
				b[i] = byte('0' + (int(orig-'0')+delta+10)%10)
				nxt := string(b)
				if !seen[nxt] && !dead[nxt] {
					seen[nxt] = true
					queue = append(queue, item{nxt, cur.steps + 1})
				}
			}
			b[i] = orig
		}
	}
	return -1
}
