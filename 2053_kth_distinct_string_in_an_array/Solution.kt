// LeetCode 2053 - Kth Distinct String in an Array
// https://leetcode.com/problems/kth-distinct-string-in-an-array/

class Solution {
    fun kthDistinct(arr: Array<String>, k: Int): String {
var freq: HashMap<String, Int> = HashMap()
for (s in arr) {
freq.merge(s, 1, { a, b -> a + b })
}
for (s in arr) {
if (freq[s] == 1 && --k == 0) {
return s
}
}
return ""
}
}
