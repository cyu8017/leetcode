// LeetCode 0126 - Word Ladder II
// https://leetcode.com/problems/word-ladder-ii/

import scala.collection.mutable

object Solution {
  def findLadders(beginWord: String, endWord: String, wordList: List[String]): List[List[String]] = {
    val words = wordList.toSet
    if (!words.contains(endWord)) return List.empty
    val parents = mutable.Map.empty[String, mutable.ListBuffer[String]]
    val visited = mutable.Set(beginWord)
    val queue = mutable.Queue(beginWord)
    var found = false

    while (queue.nonEmpty && !found) {
      val levelVisited = mutable.Set.empty[String]
      val size = queue.size
      for (_ <- 0 until size) {
        val word = queue.dequeue()
        val chars = word.toCharArray
        for (i <- chars.indices) {
          val original = chars(i)
          for (c <- 'a' to 'z') {
            chars(i) = c
            val next = chars.mkString
            if (words.contains(next) && !visited.contains(next)) {
              if (levelVisited.add(next)) queue.enqueue(next)
              parents.getOrElseUpdate(next, mutable.ListBuffer.empty) += word
              if (next == endWord) found = true
            }
          }
          chars(i) = original
        }
      }
      visited ++= levelVisited
    }

    val result = mutable.ListBuffer.empty[List[String]]
    def build(word: String, path: List[String]): Unit = {
      val nextPath = word :: path
      if (word == beginWord) result += nextPath
      else parents.getOrElse(word, mutable.ListBuffer.empty).foreach(parent => build(parent, nextPath))
    }
    if (found) build(endWord, Nil)
    result.toList
  }
}