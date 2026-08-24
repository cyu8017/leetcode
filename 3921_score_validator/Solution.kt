// LeetCode 3921 - Score Validator
// https://leetcode.com/problems/score-validator/

class Solution {
    fun scoreValidator(events: Array<String>): IntArray {
        var score = 0
        var counter = 0
        for (eventStr in events) {
            var isNum = eventStr.length > 0
            var num = 0
            var start = 0
            if (isNum && eventStr[0] == '-') start = 1
            for (i in start until eventStr.length) {
                if (eventStr[i] < '0' || eventStr[i] > '9') {
                    isNum = false
                    break
                }
                num = num * 10 + (eventStr[i] - '0')
            }
            if (isNum && !(start == 1 && eventStr.length == 1)) {
                if (start == 1) num = -num
                score += num
            } else if (eventStr.equals("W")) {
                counter++
                if (counter == 10) break
            } else {
                score++
            }
        }
        return intArrayOf( score, counter )
    }
}
