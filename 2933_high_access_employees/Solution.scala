// LeetCode 2933 - High-Access Employees
// https://leetcode.com/problems/high-access-employees/

object Solution {
  def findHighAccessEmployees(access_times: Array[Array[String]]): Array[String] = {
    val m = scala.collection.mutable.Map.empty[String, scala.collection.mutable.ArrayBuffer[Int]]
    access_times.foreach { a =>
      val name = a(0)
      val t = a(1)
      val hh = (t.charAt(0) - '0') * 10 + (t.charAt(1) - '0')
      val mm = (t.charAt(2) - '0') * 10 + (t.charAt(3) - '0')
      m.getOrElseUpdate(name, scala.collection.mutable.ArrayBuffer.empty[Int]) += hh * 60 + mm
    }
    val ans = scala.collection.mutable.ArrayBuffer.empty[String]
    m.foreach { case (name, times) =>
      val sorted = times.sorted
      var i = 0
      var found = false
      while (i + 2 < sorted.length && !found) {
        if (sorted(i + 2) - sorted(i) < 60) {
          ans += name
          found = true
        }
        i += 1
      }
    }
    ans.sorted.toArray
  }
}
