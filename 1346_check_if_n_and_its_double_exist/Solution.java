// LeetCode 1346 - Check If N And Its Double Exist
// https://leetcode.com/problems/check-if-n-and-its-double-exist/

import java.util.*;

class Solution {
    public boolean checkIfExist(int[] arr) {
        var seen = new HashSet<>();
        for (int value : arr) {
            if (seen.contains(2 * value) || (value % 2 == 0 && seen.contains(value / 2))) return true;
            seen.add(value);
        }
        return false;
    }
}
