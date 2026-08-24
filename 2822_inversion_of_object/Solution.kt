// LeetCode 2822 - Inversion of Object
// https://leetcode.com/problems/inversion-of-object/
// JS-only problem; Java string-map stand-in.

class Solution {
    fun invertObject(obj: MutableMap<String, String>): MutableMap<String, MutableList<String>> {
        var output = HashMap<String, MutableList<String>>()
        for (Map.Entry<String, String> kv : obj.entrySet()) {
            output.computeIfAbsent(kv.getValue(), k -> ArrayList()).add(kv.getKey())
        }
        return output
    }
}
