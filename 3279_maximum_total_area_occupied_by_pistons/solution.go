// LeetCode 3279 - Maximum Total Area Occupied by Pistons
// https://leetcode.com/problems/maximum-total-area-occupied-by-pistons/

func maxArea(height int, positions []int, directions string) int64 {
	n := len(positions)
	pos := append([]int(nil), positions...)
	dir := []byte(directions)
	var best int64
	for t := 0; t <= 2*height; t++ {
		var sum int64
		for i := 0; i < n; i++ {
			sum += int64(pos[i])
		}
		if sum > best {
			best = sum
		}
		for i := 0; i < n; i++ {
			if dir[i] == 'U' {
				if pos[i] == height {
					dir[i] = 'D'
					pos[i]--
				} else {
					pos[i]++
				}
			} else {
				if pos[i] == 0 {
					dir[i] = 'U'
					pos[i]++
				} else {
					pos[i]--
				}
			}
		}
	}
	return best
}
