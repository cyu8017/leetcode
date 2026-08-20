// LeetCode 2029 - Stone Game IX
// https://leetcode.com/problems/stone-game-ix/

func stoneGameIX(stones []int) bool {
	cnt := [3]int{}
	for _, s := range stones {
		cnt[s%3]++
	}
	if cnt[0]%2 == 0 {
		return cnt[1] > 0 && cnt[2] > 0
	}
	return abs2029(cnt[1]-cnt[2]) > 2
}

func abs2029(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
