// LeetCode 1441 - Build an Array With Stack Operations
// https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution {
    fun buildArray(target: IntArray, n: Int): List<String> {
        val answer = mutableListOf<String>()
        var current = 1
        for (value in target) {
            while (current < value) {
                answer.add("Push")
                answer.add("Pop")
                current++
            }
            answer.add("Push")
            current++
        }
        return answer
    }
}
