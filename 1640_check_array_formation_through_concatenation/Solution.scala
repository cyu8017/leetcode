// LeetCode 1640 - Check Array Formation Through Concatenation
// https://leetcode.com/problems/check-array-formation-through-concatenation/

object Solution {
  def canFormArray(arr: Array[Int], pieces: Array[Array[Int]]): Boolean = {
    val byFirst = pieces.map(p => p(0) -> p).toMap
    var i = 0
    while (i < arr.length) {
      byFirst.get(arr(i)) match {
        case None => return false
        case Some(p) =>
          if (!arr.slice(i, i + p.length).sameElements(p)) return false
          i += p.length
      }
    }
    true
  }
}
