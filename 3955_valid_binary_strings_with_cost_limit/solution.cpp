// LeetCode 3955 - Valid Binary Strings With Cost Limit
// https://leetcode.com/problems/valid-binary-strings-with-cost-limit/

#include <functional>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> generateValidStrings(int n, int k) {
        std::vector<std::string> ans;
        std::string path;
        path.reserve(n);
        std::function<void(int, int)> dfs = [&](int i, int tot) {
            if (i >= n) {
                ans.push_back(path);
                return;
            }
            path.push_back('0');
            dfs(i + 1, tot);
            path.pop_back();
            if ((path.empty() || path.back() == '0') && tot + i <= k) {
                path.push_back('1');
                dfs(i + 1, tot + i);
                path.pop_back();
            }
        };
        dfs(0, 0);
        return ans;
    }
};
