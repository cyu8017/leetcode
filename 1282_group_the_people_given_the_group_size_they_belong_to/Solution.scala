// LeetCode 1282 - Group the People Given the Group Size They Belong To
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

object Solution {
  def groupThePeople(groupSizes: Array[Int]): List[List[Int]] = {
    val pending = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ListBuffer[Int]]
    val answer = scala.collection.mutable.ListBuffer.empty[List[Int]]
    for (person <- groupSizes.indices) {
      val size = groupSizes(person)
      val buf = pending.getOrElseUpdate(size, scala.collection.mutable.ListBuffer.empty)
      buf += person
      if (buf.length == size) {
        answer += buf.toList
        pending(size) = scala.collection.mutable.ListBuffer.empty
      }
    }
    answer.toList
  }
}
