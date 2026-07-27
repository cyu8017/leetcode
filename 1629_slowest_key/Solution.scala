// LeetCode 1629 - Slowest Key
// https://leetcode.com/problems/slowest-key/

object Solution {
  def slowestKey(releaseTimes: Array[Int], keysPressed: String): Char = {
    var bestDur = releaseTimes(0)
    var bestKey = keysPressed.charAt(0)
    var i = 1
    while (i < releaseTimes.length) {
      val duration = releaseTimes(i) - releaseTimes(i - 1)
      val key = keysPressed.charAt(i)
      if (duration > bestDur || (duration == bestDur && key > bestKey)) {
        bestDur = duration
        bestKey = key
      }
      i += 1
    }
    bestKey
  }
}
