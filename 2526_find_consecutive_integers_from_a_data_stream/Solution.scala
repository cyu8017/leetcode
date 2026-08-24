// LeetCode 2526 - Find Consecutive Integers from a Data Stream
// https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream(_value: Int, _k: Int) {
  private val value = _value
  private val k = _k
  private var streak = 0

  def consec(num: Int): Boolean = {
    if (num == value) streak += 1
    else streak = 0
    streak >= k
  }
}
