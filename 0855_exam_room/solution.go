// LeetCode 0855 - Exam Room
// https://leetcode.com/problems/exam-room/

import "sort"

type ExamRoom struct {
	n     int
	seats []int
}

func Constructor(n int) ExamRoom {
	return ExamRoom{n: n, seats: []int{}}
}

func (this *ExamRoom) Seat() int {
	if len(this.seats) == 0 {
		this.seats = append(this.seats, 0)
		return 0
	}
	bestSeat := 0
	bestDist := this.seats[0]
	for i := 1; i < len(this.seats); i++ {
		dist := (this.seats[i] - this.seats[i-1]) / 2
		if dist > bestDist {
			bestDist = dist
			bestSeat = this.seats[i-1] + dist
		}
	}
	if this.n-1-this.seats[len(this.seats)-1] > bestDist {
		bestSeat = this.n - 1
	}
	this.seats = append(this.seats, bestSeat)
	sort.Ints(this.seats)
	return bestSeat
}

func (this *ExamRoom) Leave(p int) {
	for i, s := range this.seats {
		if s == p {
			this.seats = append(this.seats[:i], this.seats[i+1:]...)
			return
		}
	}
}
