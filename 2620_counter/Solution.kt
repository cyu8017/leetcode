// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/

class Solution {
    fun createCounter(n: Int): () -> Int {
        var cur = n
        return { cur++ }
    }
}
