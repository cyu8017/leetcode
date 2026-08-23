// LeetCode 2727 - Is Object Empty
// https://leetcode.com/problems/is-object-empty/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isEmpty(Map<String, Integer> obj) {
        return obj.size() == 0;
    }

    public boolean isEmpty(int[] arr) {
        return arr.length == 0;
    }
}
