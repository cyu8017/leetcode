// LeetCode 2766 - Relocate Marbles
// https://leetcode.com/problems/relocate-marbles/

object Solution {
  def relocateMarbles(nums: Array[Int], moveFrom: Array[Int], moveTo: Array[Int]): List[Int] = {
    val pos = scala.collection.mutable.HashSet(nums: _*)
    var i = 0
    while (i < moveFrom.length) {
      pos.remove(moveFrom(i))
      pos += moveTo(i)
      i += 1
    }
    pos.toList.sorted
  }
}
