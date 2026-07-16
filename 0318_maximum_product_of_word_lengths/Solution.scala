// LeetCode 0318 - Maximum Product of Word Lengths

// https://leetcode.com/problems/maximum-product-of-word-lengths/



object Solution {

  def maxProduct(words: Array[String]): Int = {

    val count = words.length

    val masks = new Array[Int](count)

    val lengths = new Array[Int](count)

    for (index <- 0 until count) {

      val word = words(index)

      var mask = 0

      var valid = true

      for (charIndex <- word.indices) {

        val bit = 1 << (word(charIndex) - 'a')

        if ((mask & bit) != 0) {

          valid = false

        } else {

          mask |= bit

        }

      }

      masks(index) = if (valid) mask else 0

      lengths(index) = word.length

    }



    var best = 0

    for (left <- 0 until count if masks(left) != 0) {

      for (right <- left + 1 until count if masks(right) != 0) {

        if ((masks(left) & masks(right)) == 0) {

          best = math.max(best, lengths(left) * lengths(right))

        }

      }

    }

    best

  }

}

