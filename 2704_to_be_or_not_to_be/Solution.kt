// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/

class Expect(private val `val`: Int) {
    fun toBe(other: Int): Boolean {
        if (`val` == other) return true
        throw RuntimeException("Not Equal")
    }

    fun notToBe(other: Int): Boolean {
        if (`val` != other) return true
        throw RuntimeException("Equal")
    }
}

class Solution {
    fun expect(`val`: Int): Expect = Expect(`val`)
}
