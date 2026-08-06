object Solution {
  def busyStudent(startTime: Array[Int], endTime: Array[Int], queryTime: Int): Int =
    startTime.indices.count(i => startTime(i) <= queryTime && queryTime <= endTime(i))
}
