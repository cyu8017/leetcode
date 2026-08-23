// LeetCode 2822 - Inversion of Object
// https://leetcode.com/problems/inversion-of-object/
// JS-only problem; Java string-map stand-in.

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public Map<String, List<String>> invertObject(Map<String, String> obj) {
        Map<String, List<String>> output = new HashMap<>();
        for (Map.Entry<String, String> kv : obj.entrySet()) {
            output.computeIfAbsent(kv.getValue(), k -> new ArrayList<>()).add(kv.getKey());
        }
        return output;
    }
}
