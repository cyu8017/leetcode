// LeetCode 3074 - Apple Redistribution into Boxes
// https://leetcode.com/problems/apple-redistribution-into-boxes/

object Solution {
  def minimumBoxes(apple: Array[Int], capacity: Array[Int]): Int = {
    val cap = capacity.sorted
    var s = 0
    apple.foreach(x => s += x)
    var i = 1
    while (true) {
      s -= cap(cap.length - i)
      if (s <= 0) return i
      i += 1
    }
    0
  }
}
