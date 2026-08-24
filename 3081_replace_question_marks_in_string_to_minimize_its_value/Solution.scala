// LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
// https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

object Solution {
  def minimizeStringValue(s: String): String = {
    val cnt = new Array[Int](26)
    var k = 0
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i)
      if (c == '?') k += 1
      else cnt(c - 'a') += 1
      i += 1
    }
    val pq = new java.util.PriorityQueue[Array[Int]](
      (a: Array[Int], b: Array[Int]) => if (a(0) != b(0)) a(0) - b(0) else a(1) - b(1)
    )
    i = 0
    while (i < 26) {
      pq.offer(Array(cnt(i), i))
      i += 1
    }
    val t = new Array[Int](k)
    i = 0
    while (i < k) {
      val p = pq.poll()
      t(i) = p(1)
      p(0) += 1
      pq.offer(p)
      i += 1
    }
    java.util.Arrays.sort(t)
    val arr = s.toCharArray
    var j = 0
    i = 0
    while (i < arr.length) {
      if (arr(i) == '?') {
        arr(i) = (t(j) + 'a').toChar
        j += 1
      }
      i += 1
    }
    new String(arr)
  }
}
