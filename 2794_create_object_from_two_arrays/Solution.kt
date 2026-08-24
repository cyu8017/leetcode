// LeetCode 2794 - Create Object from Two Arrays
// https://leetcode.com/problems/create-object-from-two-arrays/
// JS-only problem; C# string-map stand-in.

class Solution {
    fun createObject(keysArr: Array<String>, valuesArr: IntArray): MutableMap<String, Int> {
        var output = HashMap<Int, Int>()
        var n = minOf(keysArr.size, valuesArr.size)
        for (i in 0 until n) {
            if (!output.containsKey(keysArr[i])) output[keysArr[i]] = valuesArr[i]
        }
        return output
    }
}
