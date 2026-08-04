// LeetCode 1461 - Check If A String Contains All Binary Codes Of Size K
// https://leetcode.com/problems/check-if-a-String-contains-all-binary-codes-of-size-k/

import java.util.*;

class Solution {
    public boolean hasAllCodes(String s, int k) {
        var set = new HashSet<>();
        for (int i = 0; i <= s.length - k; i++) set.add(s.SubString(i, k));
        return set.size() == (1 << k);
    }
}
