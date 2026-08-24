// LeetCode 2271 - Maximum White Tiles Covered by a Carpet
// https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

object Solution {
  def maximumWhiteTiles(tiles: Array[Array[Int]], carpetLen: Int): Int = {
    java.util.Arrays.sort(tiles, (a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    val n = tiles.length
    val pref = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + (tiles(i)(1) - tiles(i)(0) + 1)
      i += 1
    }
    var ans = 0
    var j = 0
    i = 0
    while (i < n) {
      val end = tiles(i)(0) + carpetLen - 1
      while (j < n && tiles(j)(0) <= end) j += 1
      var cover = pref(j) - pref(i)
      if (j > 0 && tiles(j - 1)(1) > end) cover -= tiles(j - 1)(1) - end
      ans = math.max(ans, cover)
      i += 1
    }
    ans
  }
}
