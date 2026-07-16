// LeetCode 0392 - Is Subsequence

// https://leetcode.com/problems/is-subsequence/



object Solution {

  def isSubsequence(s: String, t: String): Boolean = {

    var index = 0



    for (character <- t) {

      if (index < s.length && s(index) == character) {

        index += 1

      }

    }



    index == s.length

  }

}
