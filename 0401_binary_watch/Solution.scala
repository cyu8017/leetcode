// LeetCode 0401 - Binary Watch

// https://leetcode.com/problems/binary-watch/



import scala.collection.mutable



object Solution {

  def readBinaryWatch(turnedOn: Int): List[String] = {

    val result = mutable.ListBuffer.empty[String]



    for (hour <- 0 until 12; minute <- 0 until 60) {

      if (Integer.bitCount(hour) + Integer.bitCount(minute) == turnedOn) {

        result += s"$hour:${minute.toString.reverse.padTo(2, '0').reverse}"

      }

    }



    result.toList

  }

}
