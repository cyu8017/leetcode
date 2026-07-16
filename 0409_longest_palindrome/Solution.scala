// LeetCode 0409 - Longest Palindrome

// https://leetcode.com/problems/longest-palindrome/



object Solution {

  def longestPalindrome(s: String): Int = {

    val counts = new Array[Int](128)



    for (character <- s) {

      counts(character) += 1

    }



    var length = 0

    var odd = false



    for (count <- counts) {

      if (count > 0) {

        length += count / 2 * 2

        if (count % 2 == 1) {

          odd = true

        }

      }

    }



    length + (if (odd) 1 else 0)

  }

}
