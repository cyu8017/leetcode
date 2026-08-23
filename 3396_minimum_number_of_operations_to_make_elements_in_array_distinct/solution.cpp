// LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
// https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int minimumOperations(std::vector<int>& nums) {
        int ops = 0;
        while (true) {
            std::unordered_set<int> seen;
            bool dup = false;
            for (int x : nums) {
                if (seen.count(x)) { dup = true; break; }
                seen.insert(x);
            }
            if (!dup) return ops;
            if ((int)nums.size() <= 3) return ops + 1;
            nums.erase(nums.begin(), nums.begin() + 3);
            ops++;
        }
    }
};
