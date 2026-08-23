// LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
// https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/
// JS-only problem; C++ stand-in.

#include <functional>
#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<std::pair<std::string, int>> promiseAllSettled(std::vector<std::function<int()>>& functions) {
        std::vector<std::pair<std::string, int>> ans;
        for (auto& f : functions) ans.push_back({"fulfilled", f()});
        return ans;
    }
};
