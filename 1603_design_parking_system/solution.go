// LeetCode 1603 - Design Parking System
// https://leetcode.com/problems/design-parking-system/

type ParkingSystem struct {
	spaces [4]int
}

func Constructor(big int, medium int, small int) ParkingSystem {
	return ParkingSystem{spaces: [4]int{0, big, medium, small}}
}

func (this *ParkingSystem) AddCar(carType int) bool {
	if this.spaces[carType] == 0 {
		return false
	}
	this.spaces[carType]--
	return true
}
