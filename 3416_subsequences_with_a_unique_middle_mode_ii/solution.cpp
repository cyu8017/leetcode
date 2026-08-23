// LeetCode 3416 - Subsequences with a Unique Middle Mode II
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-ii/

#include <unordered_map>
#include <vector>

class Solution {
    bool uniqueMode(const std::vector<int>& a) {
        std::unordered_map<int, int> freq;
        for (int x : a) freq[x]++;
        int best = 0, cnt = 0;
        for (auto& [_, f] : freq) {
            if (f > best) { best = f; cnt = 1; }
            else if (f == best) cnt++;
        }
        return cnt == 1;
    }

public:
    int subsequencesWithMiddleMode(std::vector<int>& nums) {
        const int mod = 1000000007;
        int n = (int)nums.size();
        int ans = 0;
        for (int mid = 2; mid < n - 2; mid++) {
            for (int a = 0; a < mid; a++) {
                for (int b = a + 1; b < mid; b++) {
                    for (int c = mid + 1; c < n; c++) {
                        for (int d = c + 1; d < n; d++) {
                            std::vector<int> seq{nums[a], nums[b], nums[mid], nums[c], nums[d]};
                            if (uniqueMode(seq)) ans = (ans + 1) % mod;
                        }
                    }
                }
            }
        }
        return ans;
    }
};
