// LeetCode 0981 - Time Based Key-Value Store
// https://leetcode.com/problems/time-based-key-value-store/

class TimeMap() {
  private val times = scala.collection.mutable.Map.empty[String, scala.collection.mutable.ArrayBuffer[Int]]
  private val vals = scala.collection.mutable.Map.empty[String, scala.collection.mutable.ArrayBuffer[String]]

  def set(key: String, value: String, timestamp: Int): Unit = {
    times.getOrElseUpdate(key, scala.collection.mutable.ArrayBuffer.empty[Int]) += timestamp
    vals.getOrElseUpdate(key, scala.collection.mutable.ArrayBuffer.empty[String]) += value
  }

  def get(key: String, timestamp: Int): String = {
    val tarr = times.getOrElse(key, return "")
    val varr = vals(key)
    var lo = 0
    var hi = tarr.length - 1
    var ans = -1
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      if (tarr(mid) <= timestamp) { ans = mid; lo = mid + 1 }
      else hi = mid - 1
    }
    if (ans < 0) "" else varr(ans)
  }
}
