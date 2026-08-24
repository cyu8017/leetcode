// LeetCode 2030 - Smallest K-Length Subsequence With Occurrences of a Letter
// https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

class Solution {
    fun smallestSubsequence(s: String, k: Int, letter: Char, repetition: Int): String {
var n: Int = s.length, remainLetter = 0
for (char c : s.toCharArray()) {
if (c == letter) {
remainLetter++
}
}
var stack: StringBuilder = StringBuilder()
var inStackLetter: Int = 0
for (i in 0 until n) {
var ch: Char = s[i]
while (stack.size > 0 && ch < stack[stack.length(] - 1) && stack.size + n - i > k) {
var top: Char = stack[stack.length(] - 1)
if (top == letter) {
if (inStackLetter + remainLetter - 1 < repetition) {
break
}
inStackLetter--
}
stack.setLength(stack.size - 1)
}
if (stack.size < k) {
if (ch == letter) {
stack.append(ch)
inStackLetter++
}
else if (k - stack.size > repetition - inStackLetter) {
stack.append(ch)
}
}
if (ch == letter) {
remainLetter--
}
}
return stack.toString()
}
}
