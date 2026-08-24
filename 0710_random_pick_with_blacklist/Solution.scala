// LeetCode 0710 - Random Pick with Blacklist
// https://leetcode.com/problems/random-pick-with-blacklist/

class Solution(_n: Int, blacklist: Array[Int]) {
  private val size = _n - blacklist.length
  private val mapping = scala.collection.mutable.HashMap.empty[Int, Int]
  private val rand = new scala.util.Random()
  {
    val black = blacklist.toSet
    var white = size
    for (b <- blacklist if b < size) {
      while (black.contains(white)) white += 1
      mapping(b) = white
      white += 1
    }
  }

  def pick(): Int = {
    val index = rand.nextInt(size)
    mapping.getOrElse(index, index)
  }
}
