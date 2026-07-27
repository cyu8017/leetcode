// LeetCode 1603 - Design Parking System
// https://leetcode.com/problems/design-parking-system/

class ParkingSystem {
    private var spaces: [Int]

    init(_ big: Int, _ medium: Int, _ small: Int) {
        spaces = [0, big, medium, small]
    }

    func addCar(_ carType: Int) -> Bool {
        if spaces[carType] == 0 { return false }
        spaces[carType] -= 1
        return true
    }
}
