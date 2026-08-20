// LeetCode 0818 - Race Car
// https://leetcode.com/problems/race-car/

func racecar(target int) int {
	type state struct{ pos, speed, steps int }
	queue := []state{{0, 1, 0}}
	seen := map[[2]int]bool{{0, 1}: true}
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur.pos == target {
			return cur.steps
		}
		nxtPos, nxtSpeed := cur.pos+cur.speed, cur.speed*2
		if !seen[[2]int{nxtPos, nxtSpeed}] && abs(nxtPos) < target*2 {
			seen[[2]int{nxtPos, nxtSpeed}] = true
			queue = append(queue, state{nxtPos, nxtSpeed, cur.steps + 1})
		}
		rev := -1
		if cur.speed <= 0 {
			rev = 1
		}
		if !seen[[2]int{cur.pos, rev}] {
			seen[[2]int{cur.pos, rev}] = true
			queue = append(queue, state{cur.pos, rev, cur.steps + 1})
		}
	}
	return -1
}
