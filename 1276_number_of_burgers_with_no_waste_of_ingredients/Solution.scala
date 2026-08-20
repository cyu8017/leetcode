// LeetCode 1276 - Number of Burgers with No Waste of Ingredients
// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

object Solution {
  def numOfBurgers(tomatoSlices: Int, cheeseSlices: Int): List[Int] = {
    val jumbo = tomatoSlices / 2 - cheeseSlices
    val small = cheeseSlices - jumbo
    if (tomatoSlices % 2 == 0 && jumbo >= 0 && small >= 0) List(jumbo, small) else List.empty
  }
}
