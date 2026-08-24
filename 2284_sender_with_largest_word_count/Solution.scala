// LeetCode 2284 - Sender With Largest Word Count
// https://leetcode.com/problems/sender-with-largest-word-count/

object Solution {
  def largestWordCount(messages: Array[String], senders: Array[String]): String = {
    val count = scala.collection.mutable.HashMap.empty[String, Int]
    var best = ""
    var bestCnt = -1
    var i = 0
    while (i < messages.length) {
      var words = 1
      var j = 0
      while (j < messages(i).length) {
        if (messages(i).charAt(j) == ' ') words += 1
        j += 1
      }
      val prev = count.getOrElse(senders(i), 0)
      count(senders(i)) = prev + words
      val c2 = count(senders(i))
      if (c2 > bestCnt || (c2 == bestCnt && senders(i).compareTo(best) > 0)) {
        bestCnt = c2
        best = senders(i)
      }
      i += 1
    }
    best
  }
}
