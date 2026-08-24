// LeetCode 3433 - Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/

object Solution {
  def countMentions(numberOfUsers: Int, events: List[List[String]]): Array[Int] = {
    val ev = events.sortWith { (a, b) =>
      val ti = a(1).toInt
      val tj = b(1).toInt
      if (ti != tj) ti < tj
      else a(0).compareTo(b(0)) > 0
    }
    val online = Array.fill(numberOfUsers)(true)
    val offlineUntil = new Array[Int](numberOfUsers)
    val ans = new Array[Int](numberOfUsers)
    ev.foreach { e =>
      val t = e(1).toInt
      var i = 0
      while (i < numberOfUsers) {
        if (!online(i) && offlineUntil(i) <= t) online(i) = true
        i += 1
      }
      if (e(0) == "OFFLINE") {
        val id = e(2).toInt
        online(id) = false
        offlineUntil(id) = t + 60
      } else {
        val msg = e(2)
        if (msg == "ALL") {
          i = 0
          while (i < numberOfUsers) { ans(i) += 1; i += 1 }
        } else if (msg == "HERE") {
          i = 0
          while (i < numberOfUsers) { if (online(i)) ans(i) += 1; i += 1 }
        } else {
          msg.split(" ").foreach { part =>
            val id = part.substring(2).toInt
            ans(id) += 1
          }
        }
      }
    }
    ans
  }
}
