// LeetCode 2214 - Minimum Health to Beat Game
// https://leetcode.com/problems/minimum-health-to-beat-game/

func minimumHealth(damage []int, armor int) int64 {
	var sum int64
	mx := 0
	for _, d := range damage {
		sum += int64(d)
		if d > mx {
			mx = d
		}
	}
	reduce := armor
	if mx < reduce {
		reduce = mx
	}
	return sum - int64(reduce) + 1
}
