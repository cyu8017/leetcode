// LeetCode 1279 - Traffic Light Controlled Intersection
// https://leetcode.com/problems/traffic-light-controlled-intersection/

import "sync"

type TrafficLight struct {
	greenRoad int
	mu        sync.Mutex
}

func Constructor() TrafficLight {
	return TrafficLight{greenRoad: 1}
}

func (this *TrafficLight) CarArrived(carId int, roadId int, direction int, turnGreen func(), crossCar func()) {
	this.mu.Lock()
	defer this.mu.Unlock()
	if roadId != this.greenRoad {
		turnGreen()
		this.greenRoad = roadId
	}
	crossCar()
}
