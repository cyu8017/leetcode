// LeetCode 0277 - Find the Celebrity
// https://leetcode.com/problems/find-the-celebrity/

fun knows(a: Int, b: Int): Boolean = false

class Solution {
    fun findCelebrity(n: Int): Int {
        var candidate = 0
        for (person in 1 until n) {
            if (knows(candidate, person)) {
                candidate = person
            }
        }
        for (person in 0 until n) {
            if (person == candidate) {
                continue
            }
            if (knows(candidate, person) || !knows(person, candidate)) {
                return -1
            }
        }
        return candidate
    }
}
