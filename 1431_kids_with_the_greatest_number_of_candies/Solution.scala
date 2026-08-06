object Solution {
  def kidsWithCandies(candies: Array[Int], extraCandies: Int): List[Boolean] = {
    val maximum = candies.max
    candies.map(_ + extraCandies >= maximum).toList
  }
}
