// LeetCode 1707 - Maximum XOR With an Element From Array
// https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

object Solution {
  def maximizeXor(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val sorted = nums.sorted
    val order = queries.indices.sortBy(i => queries(i)(1))

    val children = scala.collection.mutable.ArrayBuffer[Array[Int]](Array(-1, -1))

    def insert(num: Int): Unit = {
      var node = 0
      var bit = 31
      while (bit >= 0) {
        val b = (num >> bit) & 1
        if (children(node)(b) == -1) {
          children(node)(b) = children.size
          children += Array(-1, -1)
        }
        node = children(node)(b)
        bit -= 1
      }
    }

    val ans = Array.fill(queries.length)(-1)
    var added = 0
    for (qi <- order) {
      val x = queries(qi)(0)
      val limit = queries(qi)(1)
      while (added < sorted.length && sorted(added) <= limit) {
        insert(sorted(added))
        added += 1
      }
      if (added > 0) {
        var node = 0
        var value = 0
        var bit = 31
        while (bit >= 0) {
          val b = (x >> bit) & 1
          val want = b ^ 1
          if (children(node)(want) != -1) {
            value |= 1 << bit
            node = children(node)(want)
          } else {
            node = children(node)(b)
          }
          bit -= 1
        }
        ans(qi) = value
      }
    }
    ans
  }
}
