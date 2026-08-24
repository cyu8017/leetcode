// LeetCode 2728 - Count Houses in a Circular Street
// https://leetcode.com/problems/count-houses-in-a-circular-street/

trait Street {
  def openDoor(): Unit
  def closeDoor(): Unit
  def isDoorOpen(): Boolean
  def moveRight(): Unit
  def moveLeft(): Unit
}

object Solution {
  def countHouses(street: Street, k: Int): Int = {
    var i = 0
    while (i < k) {
      street.closeDoor()
      street.moveRight()
      i += 1
    }
    var ans = 0
    while (true) {
      ans += 1
      street.openDoor()
      street.moveRight()
      if (street.isDoorOpen()) return ans
    }
    ans
  }
}
