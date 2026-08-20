// LeetCode 0911 - Online Election
// https://leetcode.com/problems/online-election/

import "sort"

type TopVotedCandidate struct {
	times  []int
	leader []int
}

func Constructor(persons []int, times []int) TopVotedCandidate {
	counts := map[int]int{}
	leader := -1
	leaders := make([]int, len(persons))
	for i, person := range persons {
		counts[person]++
		if counts[person] >= counts[leader] {
			leader = person
		}
		leaders[i] = leader
	}
	return TopVotedCandidate{times: times, leader: leaders}
}

func (this *TopVotedCandidate) Q(t int) int {
	i := sort.Search(len(this.times), func(i int) bool {
		return this.times[i] > t
	}) - 1
	return this.leader[i]
}
