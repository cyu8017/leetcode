// LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
// https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/

func promiseAllSettled(functions []func() interface{}) []map[string]interface{} {
	ans := make([]map[string]interface{}, len(functions))
	for i, f := range functions {
		ans[i] = map[string]interface{}{"status": "fulfilled", "value": f()}
	}
	return ans
}
