// LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
// https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/

/**
 * @param {Array<Function>} functions
 * @return {Promise<Array>}
 */
var promiseAllSettled = function(functions) {
    return Promise.all(functions.map((fn) =>
        Promise.resolve().then(fn).then(
            (value) => ({status: 'fulfilled', value}),
            (reason) => ({status: 'rejected', reason})
        )
    ));
};
