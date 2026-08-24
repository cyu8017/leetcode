// LeetCode 2079 - Watering Plants
// https://leetcode.com/problems/watering-plants/

object Solution {
  def wateringPlants(plants: Array[Int], capacity: Int): Int = {
    var ans = 0
    var cur = capacity
    var i = 0
    while (i < plants.length) {
      if (cur < plants(i)) { ans += i * 2; cur = capacity }
      cur -= plants(i)
      ans += 1
      i += 1
    }
    ans
  }
}
