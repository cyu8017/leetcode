#include <numeric>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int makeConnected(int n, std::vector<std::vector<int>>& connections) {
        if ((int)connections.size() < n - 1) return -1;
        std::vector<int> parent(n);
        std::iota(parent.begin(), parent.end(), 0);
        auto find = [&](int x) {
            while (x != parent[x]) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };
        for (auto& e : connections) {
            int ra = find(e[0]), rb = find(e[1]);
            if (ra != rb) parent[ra] = rb;
        }
        std::unordered_set<int> comps;
        for (int i = 0; i < n; ++i) comps.insert(find(i));
        return (int)comps.size() - 1;
    }
};
