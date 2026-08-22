// LeetCode 3984 - Divisible Game
// https://leetcode.com/problems/divisible-game/

func divisibleGame(nums []int) int {
	candidates := map[int]struct{}{2: {}}
	for _, value := range nums {
		for divisor := 2; divisor*divisor <= value; divisor++ {
			if value%divisor != 0 {
				continue
			}
			candidates[divisor] = struct{}{}
			candidates[value/divisor] = struct{}{}
		}
		if value > 1 {
			candidates[value] = struct{}{}
		}
	}

	bestScore := -int64(^uint64(0) >> 2)
	bestK := 0
	for k := range candidates {
		var ending, score int64
		for i, value := range nums {
			contribution := -int64(value)
			if value%k == 0 {
				contribution = int64(value)
			}
			if i == 0 || ending+contribution < contribution {
				ending = contribution
			} else {
				ending += contribution
			}
			if i == 0 || ending > score {
				score = ending
			}
		}
		if score > bestScore || score == bestScore && k < bestK {
			bestScore = score
			bestK = k
		}
	}

	const mod = int64(1_000_000_007)
	answer := (bestScore % mod) * int64(bestK) % mod
	if answer < 0 {
		answer += mod
	}
	return int(answer)
}