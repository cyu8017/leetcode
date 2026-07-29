#include <unordered_set>
#include <vector>

class Solution {
public:
    bool canReach(std::vector<int>& arr, int start) {
        std::vector<int> stack{start};
        std::unordered_set<int> seen;
        while (!stack.empty()) {
            int i = stack.back();
            stack.pop_back();
            if (seen.count(i) || i < 0 || i >= (int)arr.size()) continue;
            if (arr[i] == 0) return true;
            seen.insert(i);
            stack.push_back(i - arr[i]);
            stack.push_back(i + arr[i]);
        }
        return false;
    }
};
