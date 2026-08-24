// LeetCode 0933 - Number of Recent Calls
// https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter() {
  private val q = scala.collection.mutable.Queue[Int]()

  def ping(t: Int): Int = {
    q.enqueue(t)
    while (q.front < t - 3000) q.dequeue()
    q.size
  }
}
