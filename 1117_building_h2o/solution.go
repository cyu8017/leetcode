// LeetCode 1117 - Building H2O
// https://leetcode.com/problems/building-h2o/

import "sync"

type H2O struct {
	hydrogen chan struct{}
	oxygen   chan struct{}
	mu       sync.Mutex
	count    int
}

func NewH2O() *H2O {
	h := &H2O{
		hydrogen: make(chan struct{}, 2),
		oxygen:   make(chan struct{}, 1),
	}
	h.hydrogen <- struct{}{}
	h.hydrogen <- struct{}{}
	return h
}

func (h *H2O) Hydrogen(releaseHydrogen func()) {
	<-h.hydrogen
	h.mu.Lock()
	h.count++
	if h.count == 2 {
		h.oxygen <- struct{}{}
	}
	h.mu.Unlock()
	releaseHydrogen()
}

func (h *H2O) Oxygen(releaseOxygen func()) {
	<-h.oxygen
	releaseOxygen()
	h.mu.Lock()
	h.count = 0
	h.mu.Unlock()
	h.hydrogen <- struct{}{}
	h.hydrogen <- struct{}{}
}
