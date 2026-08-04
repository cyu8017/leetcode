// LeetCode 1981 - Minimize the Difference Between Target and Chosen Elements
// https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

func minimizeTheDifference(mat [][]int, target int) int {
	possible := map[int]bool{0: true}
	for _, row := range mat {
		uniq := make(map[int]bool)
		for _, x := range row {
			uniq[x] = true
		}
		nxt := make(map[int]bool)
		for s := range possible {
			for x := range uniq {
				nxt[s+x] = true
			}
		}
		kept := make(map[int]bool)
		aboveMin := -1
		for v := range nxt {
			if v <= target {
				kept[v] = true
			} else if aboveMin == -1 || v < aboveMin {
				aboveMin = v
			}
		}
		if aboveMin != -1 {
			kept[aboveMin] = true
		}
		if len(kept) == 0 {
			mn := -1
			for v := range nxt {
				if mn == -1 || v < mn {
					mn = v
				}
			}
			kept[mn] = true
		}
		possible = kept
	}
	best := 1 << 30
	for v := range possible {
		d := v - target
		if d < 0 {
			d = -d
		}
		if d < best {
			best = d
		}
	}
	return best
}
