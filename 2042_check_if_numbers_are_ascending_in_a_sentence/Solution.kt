// LeetCode 2042 - Check if Numbers Are Ascending in a Sentence
// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution {
    fun areNumbersAscending(s: String): Boolean {
var prev: Int = -1
for (String tok : s.split(" ")) {
if (tok.isEmpty()) {
continue
}
if (tok[0] >= '0' && tok[0] <= '9') {
var v: Int = tok.toInt()
if (v <= prev) {
return false
}
prev = v
}
}
return true
}
}
