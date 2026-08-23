// LeetCode 3697 - Compute Decimal Representation
// https://leetcode.com/problems/compute-decimal-representation/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int[] decimalRepresentation(int n) {
        List<Integer> ans = new ArrayList<>();
        int p = 1;
        while (n > 0) {
            int v = n % 10;
            n /= 10;
            if (v != 0) ans.add(p * v);
            p *= 10;
        }
        Collections.reverse(ans);
        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) res[i] = ans.get(i);
        return res;
    }
}
