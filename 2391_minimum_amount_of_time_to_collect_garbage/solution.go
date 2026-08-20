// LeetCode 2391 - Minimum Amount of Time to Collect Garbage
// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

func garbageCollection(garbage []string, travel []int) int {
	ans := 0
	last := map[byte]int{}
	for i, g := range garbage {
		ans += len(g)
		for j := 0; j < len(g); j++ {
			last[g[j]] = i
		}
	}
	pref := make([]int, len(travel)+1)
	for i, t := range travel {
		pref[i+1] = pref[i] + t
	}
	for _, typ := range []byte{'M', 'P', 'G'} {
		ans += pref[last[typ]]
	}
	return ans
}
