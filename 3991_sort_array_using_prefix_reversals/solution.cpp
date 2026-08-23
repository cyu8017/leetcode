// LeetCode 3991 - Sort Array Using Prefix Reversals
// https://leetcode.com/problems/sort-array-using-prefix-reversals/

#include <queue>
#include <unordered_set>
#include <utility>
#include <vector>

class Solution {
public:
    int sortArray(std::vector<int>& nums, std::vector<int>& pre) {
        int n = (int)nums.size();

        int target = 0;
        for (int i = 0; i < n; i++) target = target * 8 + i;

        int start = 0;
        for (int x : nums) start = start * 8 + x;
        if (start == target) return 0;

        std::unordered_set<int> vis{start};
        std::queue<std::pair<std::vector<int>, int>> q;
        q.push({nums, 0});

        while (!q.empty()) {
            auto [state, dist] = q.front();
            q.pop();
            int nd = dist + 1;
            for (int x : pre) {
                std::vector<int> nxt = state;
                for (int l = 0, r = x - 1; l < r; l++, r--) {
                    std::swap(nxt[l], nxt[r]);
                }
                int key = 0;
                for (int v : nxt) key = key * 8 + v;
                if (key == target) return nd;
                if (!vis.count(key)) {
                    vis.insert(key);
                    q.push({std::move(nxt), nd});
                }
            }
        }
        return -1;
    }
};
