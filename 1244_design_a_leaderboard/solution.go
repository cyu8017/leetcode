// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

import "sort"

type Leaderboard struct {
	scores map[int]int
}

func Constructor() Leaderboard {
	return Leaderboard{scores: map[int]int{}}
}

func (this *Leaderboard) AddScore(playerId int, score int) {
	this.scores[playerId] += score
}

func (this *Leaderboard) Top(K int) int {
	vals := make([]int, 0, len(this.scores))
	for _, v := range this.scores {
		vals = append(vals, v)
	}
	sort.Sort(sort.Reverse(sort.IntSlice(vals)))
	sum := 0
	for i := 0; i < K && i < len(vals); i++ {
		sum += vals[i]
	}
	return sum
}

func (this *Leaderboard) Reset(playerId int) {
	delete(this.scores, playerId)
}
