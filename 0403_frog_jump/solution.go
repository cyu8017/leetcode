// LeetCode 0403 - Frog Jump
// https://leetcode.com/problems/frog-jump/

func canCross(stones []int) bool {
	stoneSet := make(map[int]struct{}, len(stones))
	jumps := make(map[int]map[int]struct{}, len(stones))

	for _, stone := range stones {
		stoneSet[stone] = struct{}{}
		jumps[stone] = make(map[int]struct{})
	}
	jumps[0][0] = struct{}{}

	for _, stone := range stones {
		for jump := range jumps[stone] {
			for _, nextJump := range []int{jump - 1, jump, jump + 1} {
				if nextJump <= 0 {
					continue
				}
				nextStone := stone + nextJump
				if _, ok := stoneSet[nextStone]; ok {
					jumps[nextStone][nextJump] = struct{}{}
				}
			}
		}
	}

	return len(jumps[stones[len(stones)-1]]) > 0
}
