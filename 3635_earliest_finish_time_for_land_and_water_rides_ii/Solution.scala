// LeetCode 3635 - Earliest Finish Time for Land and Water Rides II
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

object Solution {
  private def calc(a1: Array[Int], t1: Array[Int], a2: Array[Int], t2: Array[Int]): Int = {
    var minEnd = Int.MaxValue
    var i = 0
    while (i < a1.length) {
      minEnd = math.min(minEnd, a1(i) + t1(i))
      i += 1
    }
    var ans = Int.MaxValue
    i = 0
    while (i < a2.length) {
      ans = math.min(ans, math.max(minEnd, a2(i)) + t2(i))
      i += 1
    }
    ans
  }

  def earliestFinishTime(landStartTime: Array[Int], landDuration: Array[Int], waterStartTime: Array[Int], waterDuration: Array[Int]): Int = {
    math.min(
      calc(landStartTime, landDuration, waterStartTime, waterDuration),
      calc(waterStartTime, waterDuration, landStartTime, landDuration)
    )
  }
}
