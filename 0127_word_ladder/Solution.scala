// LeetCode 0127 - Word Ladder
// https://leetcode.com/problems/word-ladder/

import scala.collection.mutable

object Solution {
  def ladderLength(beginWord: String, endWord: String, wordList: List[String]): Int = {
    val words = wordList.toSet
    if (!words.contains(endWord)) return 0
    val queue = mutable.Queue(beginWord)
    val visited = mutable.Set(beginWord)
    var steps = 1
    while (queue.nonEmpty) {
      val size = queue.size
      for (_ <- 0 until size) {
        val word = queue.dequeue()
        if (word == endWord) return steps
        val chars = word.toCharArray
        for (i <- chars.indices) {
          val original = chars(i)
          for (c <- 'a' to 'z') {
            chars(i) = c
            val next = chars.mkString
            if (words.contains(next) && visited.add(next)) queue.enqueue(next)
          }
          chars(i) = original
        }
      }
      steps += 1
    }
    0
  }
}