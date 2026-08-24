// LeetCode 2979 - Most Expensive Item That Can Not Be Bought
// https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/

object Solution {
  def mostExpensiveItem(primeOne: Int, primeTwo: Int): Int =
    primeOne * primeTwo - primeOne - primeTwo
}
