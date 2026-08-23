// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

import java.util.function.IntSupplier;
import java.util.function.Supplier;

// JS timeout cancellation stand-in
class Solution {
    public Object[] cancellable(IntSupplier fn, int t) {
        boolean[] cancelled = new boolean[] {false};
        Runnable cancel = () -> cancelled[0] = true;
        Supplier<Integer> result = () -> {
            if (cancelled[0]) return null;
            return fn.getAsInt();
        };
        return new Object[] {cancel, result};
    }
}
