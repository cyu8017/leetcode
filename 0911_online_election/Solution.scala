// LeetCode 0911 - Online Election
// https://leetcode.com/problems/online-election/

class TopVotedCandidate(_persons: Array[Int], _times: Array[Int]) {
  private val times = _times
  private val leaders = Array.ofDim[Int](_persons.length)

  {
    val counts = scala.collection.mutable.Map.empty[Int, Int]
    var leader = -1
    var i = 0
    while (i < _persons.length) {
      counts(_persons(i)) = counts.getOrElse(_persons(i), 0) + 1
      if (leader == -1 || counts(_persons(i)) >= counts(leader)) leader = _persons(i)
      leaders(i) = leader
      i += 1
    }
  }

  def q(t: Int): Int = {
    var lo = 0
    var hi = times.length - 1
    while (lo <= hi) {
      val mid = (lo + hi) >>> 1
      if (times(mid) <= t) lo = mid + 1
      else hi = mid - 1
    }
    leaders(hi)
  }
}
