// LeetCode 0982 - Triples with Bitwise AND Equal To Zero
// https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int countTriplets(std::vector<int>& nums) {
        std::unordered_map<int, int> cnt;
        for (int a : nums)
            for (int b : nums) cnt[a & b]++;
        int ans = 0;
        for (int c : nums)
            for (auto& [ab, times] : cnt)
                if ((ab & c) == 0) ans += times;
        return ans;
    }
};
