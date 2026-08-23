// LeetCode 2899 - Last Visited Integers
// https://leetcode.com/problems/last-visited-integers/

#include <vector>

class Solution {
public:
    std::vector<int> lastVisitedIntegers(std::vector<int>& nums) {
        std::vector<int> seen, ans;
        int k = 0;
        for (int v : nums) {
            if (v != -1) {
                seen.push_back(v);
                k = 0;
            } else {
                k++;
                if (k > (int)seen.size()) ans.push_back(-1);
                else ans.push_back(seen[(int)seen.size() - k]);
            }
        }
        return ans;
    }
};
