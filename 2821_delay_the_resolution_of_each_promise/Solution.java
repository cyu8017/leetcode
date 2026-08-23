// LeetCode 2821 - Delay the Resolution of Each Promise
// https://leetcode.com/problems/delay-the-resolution-of-each-promise/
// JS-only problem; Java stand-in wrapping callables.

import java.util.ArrayList;
import java.util.List;
import java.util.function.IntSupplier;

class Solution {
    public List<IntSupplier> delayAll(List<IntSupplier> functions, int ms) {
        return new ArrayList<>(functions);
    }
}
