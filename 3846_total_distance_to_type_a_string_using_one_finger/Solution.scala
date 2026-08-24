// LeetCode 3846 - Total Distance To Type A String Using One Finger
// https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

object Solution {
  private val POS: Map[Char, Array[Int]] = {
    val pos = scala.collection.mutable.Map.empty[Char, Array[Int]]
    val keys = Array("qwertyuiop", "asdfghjkl", "zxcvbnm")
    var i = 0
    while (i < 3) {
      var j = 0
      while (j < keys(i).length) {
        pos(keys(i).charAt(j)) = Array(i, j)
        j += 1
      }
      i += 1
    }
    pos.toMap
  }

  def totalDistance(s: String): Int = {
    var pre = 'a'
    var ans = 0
    s.foreach { cur =>
      val p1 = POS(pre)
      val p2 = POS(cur)
      ans += math.abs(p1(0) - p2(0)) + math.abs(p1(1) - p2(1))
      pre = cur
    }
    ans
  }
}
