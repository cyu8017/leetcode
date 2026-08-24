// LeetCode 3690 - Split and Merge Array Transformation
// https://leetcode.com/problems/split-and-merge-array-transformation/

object Solution {
  def minSplitMerge(nums1: Array[Int], nums2: Array[Int]): Int = {
    val n = nums1.length

    def toArr(nums: java.util.List[Integer]): Array[Int] = {
      val t = new Array[Int](6)
      var i = 0
      while (i < n) {
        t(i) = nums.get(i)
        i += 1
      }
      t
    }

    def key(a: Array[Int]): String = java.util.Arrays.toString(a)

    val startL = new java.util.ArrayList[Integer]()
    val targetL = new java.util.ArrayList[Integer]()
    var i = 0
    while (i < n) {
      startL.add(nums1(i))
      targetL.add(nums2(i))
      i += 1
    }
    val start = toArr(startL)
    val target = toArr(targetL)
    val vis = new java.util.HashSet[String]()
    vis.add(key(start))
    var q = new java.util.ArrayList[Array[Int]]()
    q.add(start)
    var ans = 0
    while (true) {
      val nq = new java.util.ArrayList[Array[Int]]()
      val qit = q.iterator()
      while (qit.hasNext) {
        val cur = qit.next()
        if (java.util.Arrays.equals(cur, target)) return ans
        var l = 0
        while (l < n) {
          var r = l
          while (r < n) {
            val remain = new java.util.ArrayList[Integer]()
            val sub = new java.util.ArrayList[Integer]()
            i = 0
            while (i < l) {
              remain.add(cur(i))
              i += 1
            }
            i = r + 1
            while (i < n) {
              remain.add(cur(i))
              i += 1
            }
            i = l
            while (i <= r) {
              sub.add(cur(i))
              i += 1
            }
            var pos = 0
            while (pos <= remain.size()) {
              val nxtSlice = new java.util.ArrayList[Integer]()
              nxtSlice.addAll(remain.subList(0, pos))
              nxtSlice.addAll(sub)
              nxtSlice.addAll(remain.subList(pos, remain.size()))
              val nxt = toArr(nxtSlice)
              val kk = key(nxt)
              if (!vis.contains(kk)) {
                vis.add(kk)
                nq.add(nxt)
              }
              pos += 1
            }
            r += 1
          }
          l += 1
        }
      }
      q = nq
      ans += 1
    }
    -1
  }
}
