// LeetCode 1710 - Maximum Units on a Truck
// https://leetcode.com/problems/maximum-units-on-a-truck/

object Solution {
  def maximumUnits(boxTypes: Array[Array[Int]], truckSize: Int): Int = {
    val sorted = boxTypes.sortBy(-_(1))
    var remaining = truckSize
    var total = 0
    var i = 0
    while (i < sorted.length && remaining > 0) {
      val take = math.min(sorted(i)(0), remaining)
      total += take * sorted(i)(1)
      remaining -= take
      i += 1
    }
    total
  }
}
