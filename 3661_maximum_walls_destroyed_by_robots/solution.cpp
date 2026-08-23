// LeetCode 3661 - Maximum Walls Destroyed by Robots
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

#include <algorithm>
#include <map>
#include <vector>

class Solution {
public:
    int maxWalls(std::vector<int>& robots, std::vector<int>& distance, std::vector<int>& walls) {
        int n = (int)robots.size();
        std::vector<std::pair<int, int>> arr(n);
        for (int i = 0; i < n; i++) arr[i] = {robots[i], distance[i]};
        std::sort(arr.begin(), arr.end());
        std::sort(walls.begin(), walls.end());
        std::map<std::pair<int, int>, int> f;
        auto dfs = [&](auto&& self, int i, int j) -> int {
            if (i < 0) return 0;
            auto key = std::make_pair(i, j);
            if (f.count(key)) return f[key];
            int left = arr[i].first - arr[i].second;
            if (i > 0) left = std::max(left, arr[i - 1].first + 1);
            int l = (int)(std::lower_bound(walls.begin(), walls.end(), left) - walls.begin());
            int r = (int)(std::lower_bound(walls.begin(), walls.end(), arr[i].first + 1) - walls.begin());
            int ans = self(self, i - 1, 0) + (r - l);
            int right = arr[i].first + arr[i].second;
            if (i + 1 < n) {
                if (j == 0) right = std::min(right, arr[i + 1].first - arr[i + 1].second - 1);
                else right = std::min(right, arr[i + 1].first - 1);
            }
            l = (int)(std::lower_bound(walls.begin(), walls.end(), arr[i].first) - walls.begin());
            r = (int)(std::lower_bound(walls.begin(), walls.end(), right + 1) - walls.begin());
            ans = std::max(ans, self(self, i - 1, 1) + (r - l));
            return f[key] = ans;
        };
        return dfs(dfs, n - 1, 1);
    }
};
