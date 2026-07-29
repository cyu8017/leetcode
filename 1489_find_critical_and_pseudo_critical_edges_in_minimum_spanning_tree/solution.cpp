#include <algorithm>
#include <climits>
#include <numeric>
#include <tuple>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> findCriticalAndPseudoCriticalEdges(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::tuple<int,int,int,int>> es;
        for (int i = 0; i < (int)edges.size(); ++i)
            es.push_back({edges[i][2], edges[i][0], edges[i][1], i});
        std::sort(es.begin(), es.end());
        auto mst = [&](int skip = -1, int force = -1) -> long long {
            std::vector<int> parent(n);
            std::iota(parent.begin(), parent.end(), 0);
            auto find = [&](int x) {
                while (x != parent[x]) { parent[x] = parent[parent[x]]; x = parent[x]; }
                return x;
            };
            long long total = 0;
            int used = 0;
            if (force >= 0) {
                auto [w, a, b, _] = es[force];
                parent[find(a)] = find(b);
                total += w; ++used;
            }
            for (int j = 0; j < (int)es.size(); ++j) {
                if (j == skip || j == force) continue;
                auto [w, a, b, _] = es[j];
                int x = find(a), y = find(b);
                if (x != y) { parent[x] = y; total += w; ++used; }
            }
            return used == n - 1 ? total : LLONG_MAX / 4;
        };
        long long base = mst();
        std::vector<int> critical, pseudo;
        for (int j = 0; j < (int)es.size(); ++j) {
            if (mst(j) > base) critical.push_back(std::get<3>(es[j]));
            else if (mst(-1, j) == base) pseudo.push_back(std::get<3>(es[j]));
        }
        std::sort(critical.begin(), critical.end());
        std::sort(pseudo.begin(), pseudo.end());
        return {critical, pseudo};
    }
};
