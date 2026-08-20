// LeetCode 2453 - Destroy Sequential Targets
// https://leetcode.com/problems/destroy-sequential-targets/

func destroyTargets(nums []int, space int) int {
	cnt := map[int]int{}
	for _, x := range nums {
		cnt[x%space]++
	}
	bestMod, bestCnt := -1, 0
	for mod, c := range cnt {
		if c > bestCnt {
			bestCnt = c
			bestMod = mod
		}
	}
	ans := int(1e9)
	for _, x := range nums {
		if x%space == bestMod && x < ans {
			ans = x
		}
	}
	// if ties in count, need smallest nums among mods with max count
	for mod, c := range cnt {
		if c == bestCnt {
			for _, x := range nums {
				if x%space == mod && x < ans {
					ans = x
				}
			}
		}
	}
	return ans
}
