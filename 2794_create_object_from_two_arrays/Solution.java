// LeetCode 2794 - Create Object from Two Arrays
// https://leetcode.com/problems/create-object-from-two-arrays/
// JS-only problem; C# string-map stand-in.

import java.util.HashMap;
import java.util.Map;

class Solution {
    public Map<String, Integer> createObject(String[] keysArr, int[] valuesArr) {
        var output = new HashMap<String, Integer>();
        int n = Math.min(keysArr.length, valuesArr.length);
        for (int i = 0; i < n; i++) {
            if (!output.containsKey(keysArr[i])) output.put(keysArr[i], valuesArr[i]);
        }
        return output;
    }
}
