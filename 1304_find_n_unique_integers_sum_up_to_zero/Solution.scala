// LeetCode 1304 - Find N Unique Integers Sum Up To Zero
// https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

object Solution {
  def sumZero(n: Int): Array[Int] = {
    val answer = scala.collection.mutable.ArrayBuffer[Int]()
    for (value <- 1 to n / 2) {
      answer += -value
      answer += value
    }
    if (n % 2 == 1) answer += 0
    answer.toArray
  }
}
