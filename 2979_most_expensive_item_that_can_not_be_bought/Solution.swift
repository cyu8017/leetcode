// LeetCode 2979 - Most Expensive Item That Can Not Be Bought
// https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/

class Solution {
    func mostExpensiveItem(_ primeOne: Int, _ primeTwo: Int) -> Int {
        return primeOne * primeTwo - primeOne - primeTwo
    }
}
