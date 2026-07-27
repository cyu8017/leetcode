// LeetCode 1603 - Design Parking System
// https://leetcode.com/problems/design-parking-system/

class ParkingSystem(big: Int, medium: Int, small: Int) {
    private val spaces = intArrayOf(0, big, medium, small)

    fun addCar(carType: Int): Boolean {
        if (spaces[carType] == 0) return false
        spaces[carType]--
        return true
    }
}
