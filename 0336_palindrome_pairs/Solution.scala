// LeetCode 0336 - Palindrome Pairs

// https://leetcode.com/problems/palindrome-pairs/



import scala.collection.mutable



object Solution {

  def palindromePairs(words: Array[String]): List[List[Int]] = {

    val wordMap = words.zipWithIndex.toMap

    val result = mutable.Set.empty[(Int, Int)]



    for ((index, word) <- words.zipWithIndex) {

      for (split <- 0 to word.length) {

        val left = word.substring(0, split)

        val right = word.substring(split)

        if (left == left.reverse) {

          val reversedRight = right.reverse

          wordMap.get(reversedRight).foreach { otherIndex =>

            if (otherIndex != index) {

              result.add((otherIndex, index))

            }

          }

        }

        if (right == right.reverse) {

          val reversedLeft = left.reverse

          wordMap.get(reversedLeft).foreach { otherIndex =>

            if (otherIndex != index) {

              result.add((index, otherIndex))

            }

          }

        }

      }

    }



    result.map { case (left, right) => List(left, right) }.toList

  }

}
