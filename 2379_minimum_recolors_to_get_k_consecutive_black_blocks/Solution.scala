// LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

object Solution {
  def minimumRecolors(blocks: String, k: Int): Int = {
    var white = 0
    var i = 0
    while (i < k) {
      if (blocks.charAt(i) == 'W') white += 1
      i += 1
    }
    var ans = white
    i = k
    while (i < blocks.length) {
      if (blocks.charAt(i) == 'W') white += 1
      if (blocks.charAt(i - k) == 'W') white -= 1
      ans = math.min(ans, white)
      i += 1
    }
    ans
  }
}
