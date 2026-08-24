// LeetCode 2085 - Count Common Words With One Occurrence
// https://leetcode.com/problems/count-common-words-with-one-occurrence/

class Solution {
    fun countWords(words1: Array<String>, words2: Array<String>): Int {
var f1: HashMap<String, Int> = HashMap()
var f2: HashMap<String, Int> = HashMap()
for (w in words1) {
f1.merge(w, 1, { a, b -> a + b })
}
for (w in words2) {
f2.merge(w, 1, { a, b -> a + b })
}
var ans: Int = 0
for (kv in f1) {
if (kv.value == 1 && f2.getOrDefault(kv.key, 0) == 1) {
ans++
}
}
return ans
}
}
