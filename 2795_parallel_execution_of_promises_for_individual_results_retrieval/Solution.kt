// LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
// https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/
// JS-only problem; Java stand-in.

import java.util.function.IntSupplier

class Solution {
    fun promiseAllSettled(functions: MutableList<IntSupplier>): MutableList<Array<Any>> {
        val ans = ArrayList<Array<Any>>()
        for (f in functions) ans.add(arrayOf("fulfilled", f.asInt))
        return ans
    }
}
