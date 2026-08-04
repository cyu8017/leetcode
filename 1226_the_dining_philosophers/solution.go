// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

import "sync"

type DiningPhilosophers struct {
	forks [5]sync.Mutex
}

func Constructor() *DiningPhilosophers {
	return &DiningPhilosophers{}
}

func (d *DiningPhilosophers) WantsToEat(philosopher int, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork func()) {
	left, right := philosopher, (philosopher+1)%5
	first, second := left, right
	if philosopher%2 != 0 {
		first, second = right, left
	}
	d.forks[first].Lock()
	d.forks[second].Lock()
	pickLeftFork()
	pickRightFork()
	eat()
	putLeftFork()
	putRightFork()
	d.forks[second].Unlock()
	d.forks[first].Unlock()
}
