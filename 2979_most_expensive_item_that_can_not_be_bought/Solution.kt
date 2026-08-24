// LeetCode 2979 - Most Expensive Item That Can Not Be Bought
// https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/

class Solution {
    fun mostExpensiveItem(primeOne: Int, primeTwo: Int): Int {
        return primeOne * primeTwo - primeOne - primeTwo
    }
}
