// LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
// https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

object Solution {
  private val MX = 1000001
  private var factorsCache: Array[java.util.List[Integer]] = null

  private def factors(): Array[java.util.List[Integer]] = {
    if (factorsCache == null) {
      factorsCache = Array.fill[java.util.List[Integer]](MX)(new java.util.ArrayList[Integer]())
      var i = 2
      while (i < MX) {
        if (factorsCache(i).isEmpty) {
          var j = i
          while (j < MX) {
            factorsCache(j).add(i)
            j += i
          }
        }
        i += 1
      }
    }
    factorsCache
  }

  def minJumps(nums: Array[Int]): Int = {
    val fac = factors()
    val n = nums.length
    val g = new java.util.HashMap[Integer, java.util.List[Integer]]()
    var i = 0
    while (i < n) {
      val it = fac(nums(i)).iterator()
      while (it.hasNext) {
        val p = it.next()
        g.computeIfAbsent(p, (_: Integer) => new java.util.ArrayList[Integer]()).add(i)
      }
      i += 1
    }
    var ans = 0
    val vis = new Array[Boolean](n)
    vis(0) = true
    var q = new java.util.ArrayList[Integer]()
    q.add(0)
    while (true) {
      val nq = new java.util.ArrayList[Integer]()
      val itq = q.iterator()
      while (itq.hasNext) {
        val ii = itq.next().intValue()
        if (ii == n - 1) return ans
        val idx = new java.util.ArrayList[Integer](g.getOrDefault(nums(ii), java.util.List.of[Integer]()))
        idx.add(ii + 1)
        if (ii > 0) idx.add(ii - 1)
        val itj = idx.iterator()
        while (itj.hasNext) {
          val j = itj.next().intValue()
          if (j >= 0 && j < n && !vis(j)) {
            vis(j) = true
            nq.add(j)
          }
        }
        g.put(nums(ii), new java.util.ArrayList[Integer]())
      }
      q = nq
      ans += 1
    }
    -1
  }
}
