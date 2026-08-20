// LeetCode 0957 - Prison Cells After N Days
// https://leetcode.com/problems/prison-cells-after-n-days/

func prisonAfterNDays(cells []int, n int) []int {
	seen := map[[8]int]int{}
	var state [8]int
	copy(state[:], cells)
	for n > 0 {
		if prev, ok := seen[state]; ok {
			cycle := prev - n
			n %= cycle
			if n == 0 {
				break
			}
		}
		seen[state] = n
		var nxt [8]int
		for i := 1; i < 7; i++ {
			if state[i-1] == state[i+1] {
				nxt[i] = 1
			}
		}
		state = nxt
		n--
	}
	return state[:]
}
