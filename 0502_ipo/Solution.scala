// LeetCode 0502 - IPO
// https://leetcode.com/problems/ipo/

import scala.collection.mutable

object Solution {
  private implicit object ProfitOrdering extends Ordering[Int] {
    override def compare(x: Int, y: Int): Int = y.compareTo(x)
  }

  def findMaximizedCapital(k: Int, w: Int, profits: Array[Int], capital: Array[Int]): Int = {
    val projects = capital.indices.map(index => (capital(index), profits(index))).sortBy(_._1)
    val available = mutable.PriorityQueue.empty[Int]
    var wealth = w
    var projectIndex = 0
    for (_ <- 0 until k) {
      while (projectIndex < projects.length && projects(projectIndex)._1 <= wealth) {
        available.enqueue(projects(projectIndex)._2)
        projectIndex += 1
      }
      if (available.isEmpty) return wealth
      wealth += available.dequeue()
    }
    wealth
  }
}
