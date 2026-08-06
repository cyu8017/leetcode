// LeetCode 1311 - Get Watched Videos By Your Friends
// https://leetcode.com/problems/get-watched-videos-by-your-friends/

object Solution {
  def watchedVideosByFriends(
    watchedVideos: List[List[String]],
    friends: Array[Array[Int]],
    id: Int,
    level: Int
  ): List[String] = {
    val queue = scala.collection.mutable.ArrayDeque[(Int, Int)]()
    val seen = scala.collection.mutable.HashSet(id)
    queue.append((id, 0))
    val people = scala.collection.mutable.ArrayBuffer[Int]()
    while (queue.nonEmpty) {
      val (person, distance) = queue.removeHead()
      if (distance == level) people += person
      else {
        for (friend <- friends(person) if !seen.contains(friend)) {
          seen += friend
          queue.append((friend, distance + 1))
        }
      }
    }
    val counts = scala.collection.mutable.HashMap[String, Int]()
    for (person <- people; video <- watchedVideos(person)) {
      counts(video) = counts.getOrElse(video, 0) + 1
    }
    counts.keys.toList.sortBy(v => (counts(v), v))
  }
}
