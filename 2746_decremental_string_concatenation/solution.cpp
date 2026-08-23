// LeetCode 2746 - Decremental String Concatenation
// https://leetcode.com/problems/decremental-string-concatenation/

#include <vector>
#include <string>
#include <functional>
#include <map>
#include <tuple>
#include <algorithm>

class Solution {
public:
    int minimizeConcatenatedLength(std::vector<std::string>& words) {
        int n = (int)words.size();
        std::map<std::tuple<int,char,char>, int> memo;
        std::function<int(int,char,char)> dfs = [&](int i, char first, char last) -> int {
            if (i == n) return 0;
            auto key = std::make_tuple(i, first, last);
            if (memo.count(key)) return memo[key];
            auto& w = words[i];
            char wf = w.front(), wl = w.back();
            int add1 = (int)w.size() - (last == wf ? 1 : 0);
            int add2 = (int)w.size() - (wl == first ? 1 : 0);
            int a = add1 + dfs(i + 1, first, wl);
            int b = add2 + dfs(i + 1, wf, last);
            return memo[key] = std::min(a, b);
        };
        auto& w0 = words[0];
        return (int)w0.size() + dfs(1, w0.front(), w0.back());
    }
};
