// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/

import java.util.function.IntSupplier;

// JS addTwoPromises stand-in
class Solution {
    public int addTwoPromises(IntSupplier promise1, IntSupplier promise2) {
        return promise1.getAsInt() + promise2.getAsInt();
    }
}
