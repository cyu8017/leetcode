// LeetCode 2502 - Design Memory Allocator
// https://leetcode.com/problems/design-memory-allocator/

type Allocator struct {
	mem []int
}

func Constructor(n int) Allocator {
	return Allocator{mem: make([]int, n)}
}

func (a *Allocator) Allocate(size int, mID int) int {
	free := 0
	for i := 0; i < len(a.mem); i++ {
		if a.mem[i] == 0 {
			free++
			if free == size {
				start := i - size + 1
				for j := start; j <= i; j++ {
					a.mem[j] = mID
				}
				return start
			}
		} else {
			free = 0
		}
	}
	return -1
}

func (a *Allocator) FreeMemory(mID int) int {
	cnt := 0
	for i := range a.mem {
		if a.mem[i] == mID {
			a.mem[i] = 0
			cnt++
		}
	}
	return cnt
}
