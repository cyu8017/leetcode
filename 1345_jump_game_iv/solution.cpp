#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int minJumps(std::vector<int>& arr) {
        int n = (int)arr.size();
        std::unordered_map<int, std::vector<int>> positions;
        for (int i = 0; i < n; ++i) positions[arr[i]].push_back(i);
        std::queue<int> q;
        std::unordered_set<int> seen{0};
        q.push(0);
        int steps = 0;
        while (!q.empty()) {
            int sz = (int)q.size();
            for (int t = 0; t < sz; ++t) {
                int i = q.front();
                q.pop();
                if (i == n - 1) return steps;
                std::vector<int> next = positions[arr[i]];
                positions.erase(arr[i]);
                next.push_back(i - 1);
                next.push_back(i + 1);
                for (int j : next) {
                    if (j >= 0 && j < n && !seen.count(j)) {
                        seen.insert(j);
                        q.push(j);
                    }
                }
            }
            ++steps;
        }
        return -1;
    }
};
