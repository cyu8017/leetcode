// LeetCode 3766 - Minimum Operations To Make Binary Palindrome
// https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

#include <algorithm>
#include <climits>
#include <string>
#include <vector>

class Solution {
    static std::vector<int> pals;

    static bool isPalindrome(const std::string& s) {
        int m = (int)s.size();
        for (int i = 0; i < m / 2; i++) if (s[i] != s[m - 1 - i]) return false;
        return true;
    }

    static const std::vector<int>& getPals() {
        static bool inited = false;
        if (!inited) {
            int N = 1 << 14;
            for (int i = 0; i < N; i++) {
                std::string s;
                int x = i;
                if (x == 0) s = "0";
                else {
                    while (x > 0) {
                        s.push_back(char('0' + (x & 1)));
                        x >>= 1;
                    }
                    std::reverse(s.begin(), s.end());
                }
                if (isPalindrome(s)) pals.push_back(i);
            }
            inited = true;
        }
        return pals;
    }

public:
    std::vector<int> minOperations(std::vector<int>& nums) {
        const auto& p = getPals();
        std::vector<int> ans(nums.size());
        for (int k = 0; k < (int)nums.size(); k++) {
            int x = nums[k];
            auto it = std::lower_bound(p.begin(), p.end(), x);
            int t = INT_MAX;
            if (it != p.end()) t = *it - x;
            if (it != p.begin()) t = std::min(t, x - *std::prev(it));
            ans[k] = t;
        }
        return ans;
    }
};

std::vector<int> Solution::pals;
