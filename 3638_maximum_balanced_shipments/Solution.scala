// LeetCode 3638 - Maximum Balanced Shipments
// https://leetcode.com/problems/maximum-balanced-shipments/

object Solution {
  def maxBalancedShipments(weight: Array[Int]): Int = {
    var ans = 0
    var mx = 0
    weight.foreach { x =>
      mx = math.max(mx, x)
      if (x < mx) {
        ans += 1
        mx = 0
      }
    }
    ans
  }
}
