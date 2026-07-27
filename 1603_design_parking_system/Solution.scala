// LeetCode 1603 - Design Parking System
// https://leetcode.com/problems/design-parking-system/

class ParkingSystem(_big: Int, _medium: Int, _small: Int) {
  private val spaces = Array(0, _big, _medium, _small)

  def addCar(carType: Int): Boolean = {
    if (spaces(carType) == 0) false
    else {
      spaces(carType) -= 1
      true
    }
  }
}
