# LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
# https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/

# @param {Proc[]} functions
# @return {Hash[]}
def promise_all_settled(functions)
  functions.map do |fn|
    begin
      value = fn.respond_to?(:call) ? fn.call : fn
      { "status" => "fulfilled", "value" => value }
    rescue StandardError => reason
      { "status" => "rejected", "reason" => reason }
    end
  end
end
