// LeetCode 2692 - Make Object Immutable
// https://leetcode.com/problems/make-object-immutable/

import java.util.TreeMap;

// JS makeImmutable stand-in: return copy
class Solution {
    public TreeMap<String, Integer> makeImmutable(TreeMap<String, Integer> obj) {
        return new TreeMap<>(obj);
    }
}
