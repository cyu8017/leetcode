// LeetCode 2755 - Deep Merge of Two Objects
// https://leetcode.com/problems/deep-merge-of-two-objects/
// JS-only problem; simplified string-map merge stand-in.

class Solution {
    fun deepMerge(obj1: MutableMap<String, String>, obj2: MutableMap<String, String>): MutableMap<String, String> {
        var output = HashMap(obj1)
        output.putAll(obj2)
        return output
    }
}
