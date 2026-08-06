// LeetCode 1560 - Most Visited Sector in  a Circular Track
// https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

object Solution {
  def mostVisited(n: Int, rounds: Array[Int]): List[Int] = {
    val start = rounds.head
    val end = rounds.last
    if (start <= end) (start to end).toList
    else (1 to end).toList ++ (start to n).toList
  }
}
