// LeetCode 0710 - Random Pick with Blacklist
// https://leetcode.com/problems/random-pick-with-blacklist/

import "math/rand"

type Solution struct {
	size    int
	mapping map[int]int
}

func Constructor(n int, blacklist []int) Solution {
	size := n - len(blacklist)
	black := map[int]bool{}
	for _, b := range blacklist {
		black[b] = true
	}
	whites := []int{}
	for x := size; x < n; x++ {
		if !black[x] {
			whites = append(whites, x)
		}
	}
	mapping := map[int]int{}
	wi := 0
	for _, b := range blacklist {
		if b < size {
			mapping[b] = whites[wi]
			wi++
		}
	}
	return Solution{size: size, mapping: mapping}
}

func (this *Solution) Pick() int {
	index := rand.Intn(this.size)
	if v, ok := this.mapping[index]; ok {
		return v
	}
	return index
}
