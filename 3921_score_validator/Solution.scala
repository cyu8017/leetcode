// LeetCode 3921 - Score Validator
// https://leetcode.com/problems/score-validator/

object Solution {
  def scoreValidator(events: Array[String]): Array[Int] = {
    var score = 0
    var counter = 0
    var stop = false
    events.foreach { eventStr =>
      if (!stop) {
        var isNum = eventStr.length > 0
        var num = 0
        var start = 0
        if (isNum && eventStr.charAt(0) == '-') start = 1
        var i = start
        while (i < eventStr.length && isNum) {
          if (eventStr.charAt(i) < '0' || eventStr.charAt(i) > '9') isNum = false
          else num = num * 10 + (eventStr.charAt(i) - '0')
          i += 1
        }
        if (isNum && !(start == 1 && eventStr.length == 1)) {
          if (start == 1) num = -num
          score += num
        } else if (eventStr == "W") {
          counter += 1
          if (counter == 10) stop = true
        } else {
          score += 1
        }
      }
    }
    Array(score, counter)
  }
}
