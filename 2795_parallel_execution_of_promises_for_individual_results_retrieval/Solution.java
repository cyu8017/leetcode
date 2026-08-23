// LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
// https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/
// JS-only problem; Java stand-in.

import java.util.ArrayList;
import java.util.List;
import java.util.function.IntSupplier;

class Solution {
    public List<Object[]> promiseAllSettled(List<IntSupplier> functions) {
        List<Object[]> ans = new ArrayList<>();
        for (IntSupplier f : functions) ans.add(new Object[]{"fulfilled", f.getAsInt()});
        return ans;
    }
}
