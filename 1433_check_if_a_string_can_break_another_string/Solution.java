// LeetCode 1433 - Check If A String Can Break Another String
// https://leetcode.com/problems/check-if-a-String-can-break-another-String/

import java.util.*;

class Solution {
    public boolean checkIfCanBreak(String s1, String s2) {
        char[] a = s1.toCharArray(), b = s2.toCharArray();
        Arrays.sort(a); Arrays.sort(b);
        boolean ge = true, le = true;
        for (int i = 0; i < a.length; i++) { if (a[i] < b[i]) ge = false; if (a[i] > b[i]) le = false; }
        return ge || le;
    }
}
