// LeetCode 2347 - Best Poker Hand
// https://leetcode.com/problems/best-poker-hand/

func bestHand(ranks []int, suits []byte) string {
	if suits[0] == suits[1] && suits[1] == suits[2] && suits[2] == suits[3] && suits[3] == suits[4] {
		return "Flush"
	}
	cnt := map[int]int{}
	best := 0
	for _, r := range ranks {
		cnt[r]++
		if cnt[r] > best {
			best = cnt[r]
		}
	}
	if best >= 3 {
		return "Three of a Kind"
	}
	if best == 2 {
		return "Pair"
	}
	return "High Card"
}
