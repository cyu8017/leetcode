// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/

import java.util.*;
import java.util.function.IntSupplier;

// JavaScript problem; Java stand-in (sequential execution).
class Solution {
    public int[] promisePool(List<IntSupplier> functions, int n) {
        int[] ans = new int[functions.size()];
        for (int i = 0; i < functions.size(); i++) ans[i] = functions.get(i).getAsInt();
        return ans;
    }
}
