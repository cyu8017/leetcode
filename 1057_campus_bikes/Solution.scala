// LeetCode 1057 - Campus Bikes
// https://leetcode.com/problems/campus-bikes/

object Solution {
  def assignBikes(workers: Array[Array[Int]], bikes: Array[Array[Int]]): Array[Int] = {
    val triples = (for {
      w <- workers.indices
      b <- bikes.indices
      wx = workers(w)(0); wy = workers(w)(1)
      bx = bikes(b)(0); by = bikes(b)(1)
    } yield (math.abs(wx - bx) + math.abs(wy - by), w, b)).sortBy(t => (t._1, t._2, t._3))
    val ans = Array.fill(workers.length)(-1)
    val usedBikes = scala.collection.mutable.Set.empty[Int]
    var assigned = 0
    for ((_, w, b) <- triples if assigned < workers.length) {
      if (ans(w) == -1 && !usedBikes.contains(b)) {
        ans(w) = b
        usedBikes += b
        assigned += 1
      }
    }
    ans
  }
}
