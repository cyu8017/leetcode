// LeetCode 1826 - Faulty Sensor
// https://leetcode.com/problems/faulty-sensor/

object Solution {
  def badSensor(sensor1: Array[Int], sensor2: Array[Int]): Int = {
    if (sensor1.sameElements(sensor2)) return -1

    def isDefective(correct: Array[Int], faulty: Array[Int]): Boolean = {
      val n = correct.length
      var i = 0
      while (i < n && correct(i) == faulty(i)) i += 1
      if (i == n) return false
      var j = i
      while (j < n - 1 && correct(j + 1) == faulty(j)) j += 1
      j == n - 1
    }

    val s1Bad = isDefective(sensor2, sensor1)
    val s2Bad = isDefective(sensor1, sensor2)
    if (s1Bad && s2Bad) -1
    else if (s1Bad) 1
    else if (s2Bad) 2
    else -1
  }
}
