// LeetCode 2755 - Deep Merge of Two Objects
// https://leetcode.com/problems/deep-merge-of-two-objects/
// JS-only problem; simplified string-map merge stand-in.

import java.util.HashMap;
import java.util.Map;

class Solution {
    public Map<String, String> deepMerge(Map<String, String> obj1, Map<String, String> obj2) {
        Map<String, String> output = new HashMap<>(obj1);
        output.putAll(obj2);
        return output;
    }
}
