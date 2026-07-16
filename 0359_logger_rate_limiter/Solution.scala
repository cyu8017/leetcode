// LeetCode 0359 - Logger Rate Limiter

// https://leetcode.com/problems/logger-rate-limiter/



import scala.collection.mutable



class Logger {

  private val lastPrinted = mutable.Map.empty[String, Int]



  def shouldPrintMessage(timestamp: Int, message: String): Boolean = {

    if (!lastPrinted.contains(message) || timestamp - lastPrinted(message) >= 10) {

      lastPrinted(message) = timestamp

      true

    } else {

      false

    }

  }

}
