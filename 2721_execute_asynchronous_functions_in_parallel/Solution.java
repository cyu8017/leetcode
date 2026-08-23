// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

import java.util.*;
import java.util.function.IntSupplier;

// JS promiseAll stand-in: run sync functions in order
class Solution {
    public int[] promiseAll(List<IntSupplier> functions) {
        int[] out = new int[functions.size()];
        for (int i = 0; i < functions.size(); i++) out[i] = functions.get(i).getAsInt();
        return out;
    }
}
