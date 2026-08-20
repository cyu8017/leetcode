// LeetCode 3609 - Minimum Moves to Reach Target in Grid
// https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/

func minMoves(sx int, sy int, tx int, ty int) int {
	ans := 0
	for tx > sx || ty > sy {
		if tx < sx || ty < sy {
			return -1
		}
		if tx == ty {
			return -1
		}
		if tx > ty {
			if ty > sy {
				if tx >= 2*ty {
					if tx%2 != 0 {
						return -1
					}
					tx /= 2
				} else {
					tx -= ty
				}
				ans++
			} else {
				if ty != sy {
					return -1
				}
				for tx > sx {
					if tx >= 2*ty {
						if tx%2 != 0 {
							return -1
						}
						tx /= 2
					} else {
						tx -= ty
					}
					ans++
					if tx < sx {
						return -1
					}
				}
			}
		} else {
			if tx > sx {
				if ty >= 2*tx {
					if ty%2 != 0 {
						return -1
					}
					ty /= 2
				} else {
					ty -= tx
				}
				ans++
			} else {
				if tx != sx {
					return -1
				}
				for ty > sy {
					if ty >= 2*tx {
						if ty%2 != 0 {
							return -1
						}
						ty /= 2
					} else {
						ty -= tx
					}
					ans++
					if ty < sy {
						return -1
					}
				}
			}
		}
	}
	if tx == sx && ty == sy {
		return ans
	}
	return -1
}
