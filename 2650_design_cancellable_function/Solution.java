// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/

import java.util.function.IntSupplier;

// JS cancellable generator stand-in
class Solution {
    public Object[] cancellable(IntSupplier generator) {
        boolean[] cancelled = new boolean[] {false};
        boolean[] done = new boolean[] {false};
        int[] result = new int[] {0};
        Runnable cancel = () -> cancelled[0] = true;
        IntSupplier run = () -> {
            if (!done[0]) {
                result[0] = generator.getAsInt();
                done[0] = true;
            }
            return result[0];
        };
        return new Object[] {cancel, run, cancelled};
    }
}
