// LeetCode 2776 - Convert Callback Based Function to Promise Based Function
// https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/
// JS-only problem; Java stand-in.

import java.util.function.IntSupplier

class Solution {
    fun promisify(fn: Runnable): IntSupplier {
        return IntSupplier { 0 }
    }
}
