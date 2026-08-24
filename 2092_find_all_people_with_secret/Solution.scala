// LeetCode 2092 - Find All People With Secret
// https://leetcode.com/problems/find-all-people-with-secret/

object Solution {
  def findAllPeople(n: Int, meetings: Array[Array[Int]], firstPerson: Int): List[Int] = {
    val parent = Array.tabulate(n)(i => i)
    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }
    def unite(a0: Int, b0: Int): Unit = {
      val a = find(a0)
      val b = find(b0)
      if (a != b) parent(a) = b
    }
    java.util.Arrays.sort(meetings, (a: Array[Int], b: Array[Int]) => Integer.compare(a(2), b(2)))
    val know = Array.fill(n)(false)
    know(0) = true
    know(firstPerson) = true
    unite(0, firstPerson)
    var i = 0
    while (i < meetings.length) {
      var j = i
      while (j < meetings.length && meetings(j)(2) == meetings(i)(2)) j += 1
      var k = i
      while (k < j) {
        unite(meetings(k)(0), meetings(k)(1))
        k += 1
      }
      val root0 = find(0)
      val reset = scala.collection.mutable.ArrayBuffer.empty[Int]
      k = i
      while (k < j) {
        val a = meetings(k)(0)
        val b = meetings(k)(1)
        if (find(a) != root0) {
          reset += a
          reset += b
        } else {
          know(a) = true
          know(b) = true
        }
        k += 1
      }
      reset.foreach(x => parent(x) = x)
      i = j
    }
    (0 until n).filter(i => find(i) == find(0) || know(i)).toList
  }
}
