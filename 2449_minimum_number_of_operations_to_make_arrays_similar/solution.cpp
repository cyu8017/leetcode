// LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long makeSimilar(std::vector<int>& nums, std::vector<int>& target) {
        std::sort(nums.begin(), nums.end());
        std::sort(target.begin(), target.end());
        std::vector<int> oddN, evenN, oddT, evenT;
        for (int x : nums) {
            if (x % 2 == 0) evenN.push_back(x);
            else oddN.push_back(x);
        }
        for (int x : target) {
            if (x % 2 == 0) evenT.push_back(x);
            else oddT.push_back(x);
        }
        long long ans = 0;
        for (int i = 0; i < (int)oddN.size(); i++) {
            int diff = oddN[i] - oddT[i];
            if (diff > 0) ans += diff / 2;
        }
        for (int i = 0; i < (int)evenN.size(); i++) {
            int diff = evenN[i] - evenT[i];
            if (diff > 0) ans += diff / 2;
        }
        return ans;
    }
};
