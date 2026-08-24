// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

class CounterII(init: Int) {
    private val initVal = init
    private var cur = init

    fun increment(): Int = ++cur
    fun decrement(): Int = --cur
    fun reset(): Int {
        cur = initVal
        return cur
    }
}

class Solution {
    fun createCounter(init: Int): CounterII = CounterII(init)
}
