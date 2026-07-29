// LeetCode 1980 - Find Unique Binary String
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::string findDifferentBinaryString(std::vector<std::string>& nums) {
        std::unordered_set<std::string> s(nums.begin(), nums.end());
        int n = (int)nums.size();
        for (int i = 0; i < (1 << n); i++) {
            std::string cand(n, '0');
            for (int b = 0; b < n; b++) if (i & (1 << b)) cand[n - 1 - b] = '1';
            if (!s.count(cand)) return cand;
        }
        return std::string(n, '0');
    }
};
