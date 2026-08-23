// LeetCode 2983 - Palindrome Rearrangement Queries
// https://leetcode.com/problems/palindrome-rearrangement-queries/

#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    std::vector<bool> canMakePalindromeQueries(std::string s, std::vector<std::vector<int>>& queries) {
        int n = (int)s.size();
        int m = n / 2;
        std::string t(s.begin() + m, s.end());
        std::reverse(t.begin(), t.end());
        s = std::string(s.begin(), s.begin() + m);

        std::vector<std::vector<int>> pre1(m + 1, std::vector<int>(26));
        std::vector<std::vector<int>> pre2(m + 1, std::vector<int>(26));
        std::vector<int> diff(m + 1, 0);
        for (int i = 1; i <= m; ++i) {
            pre1[i] = pre1[i - 1];
            pre2[i] = pre2[i - 1];
            ++pre1[i][s[i - 1] - 'a'];
            ++pre2[i][t[i - 1] - 'a'];
            diff[i] = diff[i - 1] + (s[i - 1] == t[i - 1] ? 0 : 1);
        }

        std::vector<bool> ans(queries.size(), false);
        for (int i = 0; i < (int)queries.size(); ++i) {
            auto& q = queries[i];
            int a = q[0], b = q[1];
            int c = n - 1 - q[3], d = n - 1 - q[2];
            ans[i] = (a <= c) ? check(pre1, pre2, diff, a, b, c, d)
                              : check(pre2, pre1, diff, c, d, a, b);
        }
        return ans;
    }

private:
    bool check(const std::vector<std::vector<int>>& pre1, const std::vector<std::vector<int>>& pre2,
               const std::vector<int>& diff, int a, int b, int c, int d) {
        if (diff[a] > 0 || diff[(int)diff.size() - 1] - diff[std::max(b, d) + 1] > 0) {
            return false;
        }
        if (d <= b) {
            return count(pre1, a, b) == count(pre2, a, b);
        }
        if (b < c) {
            return diff[c] - diff[b + 1] == 0 && count(pre1, a, b) == count(pre2, a, b) &&
                   count(pre1, c, d) == count(pre2, c, d);
        }
        auto cnt1 = sub(count(pre1, a, b), count(pre2, a, c - 1));
        auto cnt2 = sub(count(pre2, c, d), count(pre1, b + 1, d));
        return !cnt1.empty() && !cnt2.empty() && cnt1 == cnt2;
    }

    std::vector<int> count(const std::vector<std::vector<int>>& pre, int i, int j) {
        std::vector<int> cnt(26);
        for (int k = 0; k < 26; ++k) cnt[k] = pre[j + 1][k] - pre[i][k];
        return cnt;
    }

    std::vector<int> sub(const std::vector<int>& cnt1, const std::vector<int>& cnt2) {
        std::vector<int> cnt(26);
        for (int i = 0; i < 26; ++i) {
            cnt[i] = cnt1[i] - cnt2[i];
            if (cnt[i] < 0) return {};
        }
        return cnt;
    }
};
