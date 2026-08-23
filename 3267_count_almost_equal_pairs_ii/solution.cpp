// LeetCode 3267 - Count Almost Equal Pairs II
// https://leetcode.com/problems/count-almost-equal-pairs-ii/

#include <functional>
#include <string>
#include <vector>

class Solution {
    std::string padNum(int x) {
        if (x == 0) return "0";
        std::string b;
        while (x > 0) {
            b.insert(b.begin(), char('0' + x % 10));
            x /= 10;
        }
        return b;
    }

    bool canWithSwaps(std::string sa, const std::string& sb, int maxSwap) {
        std::function<bool(int, int)> dfs = [&](int start, int left) -> bool {
            if (sa == sb) return true;
            if (left == 0) return false;
            for (int i = start; i < (int)sa.size(); i++) {
                if (sa[i] == sb[i]) continue;
                for (int j = i + 1; j < (int)sa.size(); j++) {
                    if (sa[j] == sb[i]) {
                        std::swap(sa[i], sa[j]);
                        if (dfs(i + 1, left - 1)) return true;
                        std::swap(sa[i], sa[j]);
                    }
                }
                return false;
            }
            return sa == sb;
        };
        return dfs(0, maxSwap);
    }

    bool almostEqual(int a, int b) {
        std::string sa = padNum(a), sb = padNum(b);
        while (sa.size() < sb.size()) sa = "0" + sa;
        while (sb.size() < sa.size()) sb = "0" + sb;
        if (sa == sb) return true;
        return canWithSwaps(sa, sb, 2);
    }

public:
    int countPairs(std::vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < (int)nums.size(); i++)
            for (int j = i + 1; j < (int)nums.size(); j++)
                if (almostEqual(nums[i], nums[j])) ans++;
        return ans;
    }
};
