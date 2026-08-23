// LeetCode 3265 - Count Almost Equal Pairs I
// https://leetcode.com/problems/count-almost-equal-pairs-i/

#include <string>
#include <vector>

class Solution {
    std::string sprintfNum(int x) {
        if (x == 0) return "0";
        std::string b;
        while (x > 0) {
            b.insert(b.begin(), char('0' + x % 10));
            x /= 10;
        }
        return b;
    }

    bool almostEqual(int a, int b) {
        std::string sa = sprintfNum(a), sb = sprintfNum(b);
        while (sa.size() < sb.size()) sa = "0" + sa;
        while (sb.size() < sa.size()) sb = "0" + sb;
        std::vector<int> diff;
        for (int i = 0; i < (int)sa.size(); i++) {
            if (sa[i] != sb[i]) diff.push_back(i);
        }
        if (diff.empty()) return true;
        if (diff.size() != 2) return false;
        int i = diff[0], j = diff[1];
        return sa[i] == sb[j] && sa[j] == sb[i];
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
