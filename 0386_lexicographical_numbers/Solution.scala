// LeetCode 0386 - Lexicographical Numbers

// https://leetcode.com/problems/lexicographical-numbers/



import scala.collection.mutable



object Solution {

  def lexicalOrder(n: Int): List[Int] = {

    val result = mutable.ListBuffer.empty[Int]

    dfs(1, n, result)

    result.toList

  }



  private def dfs(current: Int, n: Int, result: mutable.ListBuffer[Int]): Unit = {

    if (current > n) {

      return

    }

    result += current

    dfs(current * 10, n, result)

    if (current % 10 < 9) {

      dfs(current + 1, n, result)

    }

  }

}
