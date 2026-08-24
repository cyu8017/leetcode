// LeetCode 2024 - Maximize the Confusion of an Exam
// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution {
    fun maxConsecutiveAnswers(answerKey: String, k: Int): Int {
return maxOf(maxWith(answerKey, k, 'T'), maxWith(answerKey, k, 'F'))
}

    private fun maxWith(answerKey: String, k: Int, ch: Char): Int {
var left: Int = 0
var bad: Int = 0
var best: Int = 0
for (right in 0 until answerKey.length) {
if (answerKey[right] != ch) {
bad++
}
while (bad > k) {
if (answerKey[left] != ch) {
bad--
}
left++
}
best = maxOf(best, right - left + 1)
}
return best
}
}
