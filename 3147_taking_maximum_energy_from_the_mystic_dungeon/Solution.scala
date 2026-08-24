// LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon
// https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

object Solution {
  def maximumEnergy(energy: Array[Int], k: Int): Int = {
    var ans = -(1 << 30)
    val n = energy.length
    var i = n - k
    while (i < n) {
      var j = i
      var s = 0
      while (j >= 0) {
        s += energy(j)
        ans = math.max(ans, s)
        j -= k
      }
      i += 1
    }
    ans
  }
}
