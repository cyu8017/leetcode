// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

import java.util.*;
import java.util.function.IntSupplier;

// JS interval cancellation stand-in
class Solution {
    public Object[] cancellable(IntSupplier fn, int t, int times) {
        boolean[] cancelled = new boolean[] {false};
        List<Integer> results = new ArrayList<>();
        for (int i = 0; i < times && !cancelled[0]; i++) results.add(fn.getAsInt());
        Runnable cancel = () -> cancelled[0] = true;
        int[] arr = new int[results.size()];
        for (int i = 0; i < results.size(); i++) arr[i] = results.get(i);
        return new Object[] {cancel, arr};
    }
}
