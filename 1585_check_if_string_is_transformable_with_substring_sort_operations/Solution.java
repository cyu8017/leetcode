// LeetCode 1585 - Check If String Is Transformable With Substring Sort Operations
// https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/

import java.util.*;

class Solution {
    public boolean isTransformable(String s, String t) {
        List<Integer>[] positions = new List[10];
        for (int i = 0; i < 10; i++) {
            positions[i] = new ArrayList<>();
        }
        int[] heads = new int[10];
        for (int i = 0; i < s.length(); i++) {
            positions[s.charAt(i) - '0'].add(i);
        }
        for (int i = 0; i < t.length(); i++) {
            int d = t.charAt(i) - '0';
            if (heads[d] >= positions[d].size()) {
                return false;
            }
            int index = positions[d].get(heads[d]);
            for (int smaller = 0; smaller < d; smaller++) {
                if (heads[smaller] < positions[smaller].size()
                        && positions[smaller].get(heads[smaller]) < index) {
                    return false;
                }
            }
            heads[d]++;
        }
        return true;
    }
}
