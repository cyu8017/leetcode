// LeetCode 1152 - Analyze User Website Visit Pattern
// https://leetcode.com/problems/analyze-user-website-visit-pattern/

object Solution {
  def mostVisitedPattern(username: Array[String], timestamp: Array[Int], website: Array[String]): List[String] = {
    val visits = scala.collection.mutable.Map.empty[String, scala.collection.mutable.ListBuffer[(Int, String)]]
    for (i <- username.indices) {
      visits.getOrElseUpdate(username(i), scala.collection.mutable.ListBuffer.empty) += ((timestamp(i), website(i)))
    }
    val scores = scala.collection.mutable.Map.empty[(String, String, String), Int]
    for ((_, vs) <- visits) {
      val sites = vs.sortBy(_._1).map(_._2)
      val patterns = scala.collection.mutable.Set.empty[(String, String, String)]
      for (i <- sites.indices; j <- i + 1 until sites.length; k <- j + 1 until sites.length) {
        patterns += ((sites(i), sites(j), sites(k)))
      }
      for (p <- patterns) scores(p) = scores.getOrElse(p, 0) + 1
    }
    val best = scores.minBy { case (p, c) => (-c, p._1, p._2, p._3) }._1
    List(best._1, best._2, best._3)
  }
}
