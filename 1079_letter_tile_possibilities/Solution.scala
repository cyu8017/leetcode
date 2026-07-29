// LeetCode 1079 - Letter Tile Possibilities
// https://leetcode.com/problems/letter-tile-possibilities/

object Solution {
  def numTilePossibilities(tiles: String): Int = {
    val count = scala.collection.mutable.Map.empty[Char, Int]
    tiles.foreach(ch => count(ch) = count.getOrElse(ch, 0) + 1)

    def dfs(): Int = {
      var total = 0
      for (ch <- count.keys.toList if count(ch) > 0) {
        count(ch) -= 1
        total += 1 + dfs()
        count(ch) += 1
      }
      total
    }

    dfs()
  }
}
