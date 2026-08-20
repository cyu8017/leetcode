// LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
// https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

func minGroupsForValidAssignment(balls []int) int {
	freq := map[int]int{}
	for _, b := range balls {
		freq[b]++
	}
	counts := []int{}
	minF := 1 << 30
	for _, f := range freq {
		counts = append(counts, f)
		if f < minF {
			minF = f
		}
	}
	for size := minF; size >= 1; size-- {
		ok := true
		groups := 0
		for _, c := range counts {
			g := (c + size) / (size + 1)
			if g*(size+1)-c > g {
				ok = false
				break
			}
			// each group has size or size+1
			if c/size < (c+size)/(size+1) {
				// check feasible
			}
			rem := c % (size + 1)
			g2 := c / (size + 1)
			if rem == 0 {
				groups += g2
			} else if size-rem <= g2 {
				groups += g2 + 1
			} else {
				ok = false
				break
			}
			_ = g
		}
		if ok {
			return groups
		}
	}
	return len(balls)
}
