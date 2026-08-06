// LeetCode 1500 - Design a File Sharing System
// https://leetcode.com/problems/design-a-file-sharing-system/

import scala.collection.mutable

class FileSharing(_m: Int) {
  private val owners = mutable.Map.empty[Int, mutable.SortedSet[Int]]
  private val chunks = mutable.Map.empty[Int, mutable.Set[Int]]
  private val free = mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
  private var nextId = 1

  def join(ownedChunks: Array[Int]): Int = {
    val user = if (free.nonEmpty) free.dequeue() else { val id = nextId; nextId += 1; id }
    val set = mutable.Set.from(ownedChunks)
    chunks(user) = set
    for (chunk <- ownedChunks) {
      owners.getOrElseUpdate(chunk, mutable.SortedSet.empty[Int]) += user
    }
    user
  }

  def leave(userID: Int): Unit = {
    chunks.remove(userID).foreach { set =>
      for (chunk <- set) owners.get(chunk).foreach(_ -= userID)
    }
    free.enqueue(userID)
  }

  def request(userID: Int, chunkID: Int): Array[Int] = {
    val users = owners.getOrElse(chunkID, mutable.SortedSet.empty[Int]).toArray
    if (users.nonEmpty) {
      chunks.getOrElseUpdate(userID, mutable.Set.empty[Int]) += chunkID
      owners.getOrElseUpdate(chunkID, mutable.SortedSet.empty[Int]) += userID
    }
    users
  }
}
