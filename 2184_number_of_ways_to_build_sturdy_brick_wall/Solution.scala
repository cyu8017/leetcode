// LeetCode 2184 - Number of Ways to Build Sturdy Brick Wall
// https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

object Solution {
  def buildWall(height: Int, width: Int, bricks: Array[Int]): Int = {
    val Mod = 1000000007
    val masks = scala.collection.mutable.ArrayBuffer.empty[Int]
    def gen(remain: Int, mask: Int): Unit = {
      if (remain == 0) masks += mask
      else {
        bricks.foreach { b =>
          if (b <= remain) {
            var nm = mask
            if (remain - b > 0) nm |= 1 << (remain - b)
            gen(remain - b, nm)
          }
        }
      }
    }
    gen(width, 0)
    val m = masks.length
    val compat = Array.fill(m)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 0
    while (i < m) {
      var j = 0
      while (j < m) {
        if ((masks(i) & masks(j)) == 0) compat(i) += j
        j += 1
      }
      i += 1
    }
    var dp = Array.fill(m)(1)
    var h = 1
    while (h < height) {
      val ndp = Array.fill(m)(0)
      i = 0
      while (i < m) {
        compat(i).foreach { j => ndp(j) = (ndp(j) + dp(i)) % Mod }
        i += 1
      }
      dp = ndp
      h += 1
    }
    var ans = 0
    dp.foreach(v => ans = (ans + v) % Mod)
    ans
  }
}
