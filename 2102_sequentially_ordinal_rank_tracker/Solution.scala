// LeetCode 2102 - Sequentially Ordinal Rank Tracker
// https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

class SORTracker() {
  private case class Loc(name: String, score: Int)
  private val bestOrd: Ordering[Loc] = (a: Loc, b: Loc) => {
    if (a.score != b.score) Integer.compare(a.score, b.score)
    else b.name.compareTo(a.name)
  }
  private val restOrd: Ordering[Loc] = (a: Loc, b: Loc) => {
    if (a.score != b.score) Integer.compare(b.score, a.score)
    else a.name.compareTo(b.name)
  }
  private val bestQ = new java.util.PriorityQueue[Loc](bestOrd)
  private val restQ = new java.util.PriorityQueue[Loc](restOrd)
  private var k = 0

  def add(name: String, score: Int): Unit = {
    bestQ.offer(Loc(name, score))
    if (bestQ.size > k) restQ.offer(bestQ.poll())
  }

  def get(): String = {
    k += 1
    if (!restQ.isEmpty) bestQ.offer(restQ.poll())
    bestQ.peek().name
  }
}
