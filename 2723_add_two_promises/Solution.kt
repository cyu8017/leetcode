// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/

class Solution {
    fun addTwoPromises(promise1: () -> Int, promise2: () -> Int): Int =
        promise1() + promise2()
}
