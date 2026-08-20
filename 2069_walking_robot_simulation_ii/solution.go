// LeetCode 2069 - Walking Robot Simulation II
// https://leetcode.com/problems/walking-robot-simulation-ii/

type Robot struct {
	w, h, peri, pos int
	moved           bool
}

func Constructor(width int, height int) Robot {
	return Robot{w: width, h: height, peri: 2*(width+height) - 4}
}

func (this *Robot) Step(num int) {
	this.moved = true
	this.pos = (this.pos + num) % this.peri
}

func (this *Robot) getPosDir() (int, int, string) {
	p := this.pos
	w, h := this.w, this.h
	if p == 0 {
		if !this.moved {
			return 0, 0, "East"
		}
		return 0, 0, "South"
	}
	if p <= w-1 {
		return p, 0, "East"
	}
	p -= w - 1
	if p <= h-1 {
		return w - 1, p, "North"
	}
	p -= h - 1
	if p <= w-1 {
		return w - 1 - p, h - 1, "West"
	}
	p -= w - 1
	return 0, h - 1 - p, "South"
}

func (this *Robot) GetPos() []int {
	x, y, _ := this.getPosDir()
	return []int{x, y}
}

func (this *Robot) GetDir() string {
	_, _, d := this.getPosDir()
	return d
}
