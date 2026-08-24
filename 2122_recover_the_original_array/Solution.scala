// LeetCode 2122 - Recover the Original Array
// https://leetcode.com/problems/recover-the-original-array/

object Solution {
  def recoverArray(nums: Array[Int]): Array[Int] = {
    val sorted = nums.sorted
    val n = sorted.length
    var i = 1
    while (i < n) {
      val diff = sorted(i) - sorted(0)
      if (diff != 0 && diff % 2 == 0) {
        val k = diff / 2
        val used = Array.fill(n)(false)
        used(0) = true
        used(i) = true
        val ans = scala.collection.mutable.ArrayBuffer((sorted(0) + sorted(i)) / 2)
        var l = 0
        var r = i
        var ok = true
        while (ans.length < n / 2 && ok) {
          while (l < n && used(l)) l += 1
          if (l == n) ok = false
          else {
            val need = sorted(l) + 2 * k
            while (r < n && (used(r) || sorted(r) < need)) r += 1
            if (r == n || sorted(r) != need) ok = false
            else {
              used(l) = true
              used(r) = true
              ans += sorted(l) + k
            }
          }
        }
        if (ok) return ans.toArray
      }
      i += 1
    }
    Array.empty[Int]
  }
}
