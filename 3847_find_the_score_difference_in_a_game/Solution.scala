// LeetCode 3847 - Find The Score Difference In A Game
// https://leetcode.com/problems/find-the-score-difference-in-a-game/

object Solution {
  def scoreDifference(nums: Array[Int]): Int = {
    var ans = 0
    var k = 1
    var i = 0
    while (i < nums.length) {
      if (nums(i) % 2 != 0) k = -k
      if (i % 6 == 5) k = -k
      ans += k * nums(i)
      i += 1
    }
    ans
  }
}
