// LeetCode 2000 - Reverse Prefix of Word
// https://leetcode.com/problems/reverse-prefix-of-word/

class Solution {
    fun reversePrefix(word: String, ch: Char): String {
var pos: Int = word.indexOf(ch)
if (pos < 0) {
return word
}
var arr: CharArray = word.toCharArray()
/*for*/ var l = 0, r = pos; while (l < r) {
var tmp: Char = arr[l]
arr[l] = arr[r]
arr[r] = tmp
}
return String(arr)
}
}
