// LeetCode 1103 - Distribute Candies to People
// https://leetcode.com/problems/distribute-candies-to-people/

object Solution {
  def distributeCandies(candies: Int, num_people: Int): Array[Int] = {
    val ans = Array.fill(num_people)(0)
    var remaining = candies
    var give = 1
    var i = 0
    while (remaining > 0) {
      val take = math.min(give, remaining)
      ans(i) += take
      remaining -= take
      give += 1
      i = (i + 1) % num_people
    }
    ans
  }
}
