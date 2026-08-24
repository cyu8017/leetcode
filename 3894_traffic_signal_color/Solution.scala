// LeetCode 3894 - Traffic Signal Color
// https://leetcode.com/problems/traffic-signal-color/

object Solution {
  def trafficSignal(timer: Int): String = {
    if (timer == 0) "Green"
    else if (timer == 30) "Orange"
    else if (timer > 30 && timer <= 90) "Red"
    else "Invalid"
  }
}
