// LeetCode 1396 - Design Underground System
// https://leetcode.com/problems/design-underground-system/

type UndergroundSystem struct {
	ins   map[int]checkIn
	stats map[[2]string][2]int
}

type checkIn struct {
	station string
	t       int
}

func Constructor() UndergroundSystem {
	return UndergroundSystem{ins: map[int]checkIn{}, stats: map[[2]string][2]int{}}
}

func (this *UndergroundSystem) CheckIn(id int, stationName string, t int) {
	this.ins[id] = checkIn{stationName, t}
}

func (this *UndergroundSystem) CheckOut(id int, stationName string, t int) {
	in := this.ins[id]
	delete(this.ins, id)
	key := [2]string{in.station, stationName}
	st := this.stats[key]
	this.stats[key] = [2]int{st[0] + t - in.t, st[1] + 1}
}

func (this *UndergroundSystem) GetAverageTime(startStation string, endStation string) float64 {
	st := this.stats[[2]string{startStation, endStation}]
	return float64(st[0]) / float64(st[1])
}
