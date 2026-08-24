// LeetCode 3510 - Minimum Pair Removal to Sort Array II
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

object Solution {
  def minimumPairRemoval(nums: Array[Int]): Int = {
    val n = nums.length
    var inv = 0
    var ans = 0
    val sl = new java.util.TreeSet[Array[Long]]((a: Array[Long], b: Array[Long]) => {
      if (a(0) != b(0)) java.lang.Long.compare(a(0), b(0)) else java.lang.Long.compare(a(1), b(1))
    })
    val idx = new java.util.TreeSet[Integer]()
    var i = 0
    while (i < n) { idx.add(i); i += 1 }
    i = 0
    while (i < n - 1) {
      if (nums(i) > nums(i + 1)) inv += 1
      sl.add(Array(nums(i).toLong + nums(i + 1), i.toLong))
      i += 1
    }
    while (inv > 0) {
      ans += 1
      val p = sl.pollFirst()
      val s = p(0).toInt
      i = p(1).toInt
      val j = idx.ceiling(i + 1)
      if (nums(i) > nums(j)) inv -= 1
      val h = idx.floor(i - 1)
      if (h != null) {
        if (nums(h) > nums(i)) inv -= 1
        sl.remove(Array(nums(h).toLong + nums(i), h.toLong))
        if (nums(h) > s) inv += 1
        sl.add(Array(nums(h).toLong + s, h.toLong))
      }
      val k = idx.ceiling(j + 1)
      if (k != null) {
        if (nums(j) > nums(k)) inv -= 1
        sl.remove(Array(nums(j).toLong + nums(k), j.toLong))
        if (s > nums(k)) inv += 1
        sl.add(Array(s.toLong + nums(k), i.toLong))
      }
      nums(i) = s
      idx.remove(j)
    }
    ans
  }
}
