// LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
// https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/

object Solution {
  def promiseAllSettled(functions: List[() => Int]): List[(String, Int)] =
    functions.map(f => ("fulfilled", f()))
}
