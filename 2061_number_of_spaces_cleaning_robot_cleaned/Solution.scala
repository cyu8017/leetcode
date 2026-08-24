// LeetCode 2061 - Number of Spaces Cleaning Robot Cleaned
// https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

object Solution {
  def numberOfCleanRooms(room: Array[Array[Int]]): Int = {
    val m = room.length
    val n = room(0).length
    val dirs = Array((0, 1), (1, 0), (0, -1), (-1, 0))
    val vis = scala.collection.mutable.HashSet.empty[Int]
    val cleaned = scala.collection.mutable.HashSet(0L)
    var r = 0
    var c = 0
    var d = 0
    while (vis.add(r * 10000 + c * 10 + d)) {
      val nr = r + dirs(d)._1
      val nc = c + dirs(d)._2
      if (nr >= 0 && nr < m && nc >= 0 && nc < n && room(nr)(nc) == 0) {
        r = nr
        c = nc
        cleaned += ((r.toLong << 32) ^ (c.toLong & 0xffffffffL))
      } else d = (d + 1) % 4
    }
    cleaned.size
  }
}
