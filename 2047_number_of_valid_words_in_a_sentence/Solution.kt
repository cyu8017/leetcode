// LeetCode 2047 - Number of Valid Words in a Sentence
// https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

class Solution {
    fun countValidWords(sentence: String): Int {
var ans: Int = 0
for (String tok : sentence.split(" ")) {
if (valid(tok)) {
ans++
}
}
return ans
}

    private fun valid(w: String): Boolean {
if (w.length == 0) {
return false
}
var hyphen: Int = 0
for (i in 0 until w.length) {
var c: Char = w[i]
if (c >= '0' && c <= '9') {
return false
}
if (c == '-') {
hyphen++
if (hyphen > 1 || i == 0 || i == w.length - 1) {
return false
}
if (w[i - 1] < 'a' || w[i - 1] > 'z' || w[i + 1] < 'a' || w[i + 1] > 'z') {
return false
}
}
else if (c == '!' || c == '.' || c == ',') {
if (i != w.length - 1) {
return false
}
}
else if (c < 'a' || c > 'z') {
return false
}
}
return true
}
}
