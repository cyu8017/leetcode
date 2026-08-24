// LeetCode 0969 - Pancake Sorting
// https://leetcode.com/problems/pancake-sorting/

object Solution {
  def pancakeSort(arr: Array[Int]): List[Int] = {
    val a = arr.clone()
    val ans = scala.collection.mutable.ListBuffer[Int]()
    def indexOf(v: Int): Int = {
      var i = 0
      while (i < a.length) {
        if (a(i) == v) return i
        i += 1
      }
      -1
    }
    def reverse(l0: Int, r0: Int): Unit = {
      var l = l0
      var r = r0
      while (l < r) {
        val t = a(l); a(l) = a(r); a(r) = t
        l += 1; r -= 1
      }
    }
    var size = a.length
    while (size > 1) {
      val i = indexOf(size)
      if (i != size - 1) {
        if (i > 0) {
          ans += i + 1
          reverse(0, i)
        }
        ans += size
        reverse(0, size - 1)
      }
      size -= 1
    }
    ans.toList
  }
}
