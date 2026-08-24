// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

class Solution {
    fun debounce(fn: () -> Unit, t: Int): () -> Unit = { fn() }
}
