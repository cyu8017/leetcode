// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

#include <algorithm>
#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<bool> palindromicPathQueries(int n, std::vector<std::vector<int>>& edges,
                                             std::string s, std::vector<std::string>& queries) {
        std::vector<std::vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        std::vector<int> parent(n, -2), depth(n, 0);
        parent[0] = -1;
        std::vector<int> order = {0};
        for (int i = 0; i < (int)order.size(); i++) {
            int u = order[i];
            for (int v : graph[u]) {
                if (parent[v] == -2) {
                    parent[v] = u;
                    depth[v] = depth[u] + 1;
                    order.push_back(v);
                }
            }
        }
        std::vector<int> size(n), heavy(n, -1);
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            size[u] = 1;
            for (int v : graph[u]) {
                if (parent[v] == u) {
                    size[u] += size[v];
                    if (heavy[u] == -1 || size[v] > size[heavy[u]]) heavy[u] = v;
                }
            }
        }
        std::vector<int> head(n), position(n);
        struct Chain { int node, h; };
        std::vector<Chain> stack = {{0, 0}};
        int nextPosition = 0;
        while (!stack.empty()) {
            Chain chain = stack.back();
            stack.pop_back();
            for (int u = chain.node; u != -1; u = heavy[u]) {
                head[u] = chain.h;
                position[u] = nextPosition++;
                for (int v : graph[u]) {
                    if (parent[v] == u && v != heavy[u]) stack.push_back({v, v});
                }
            }
        }
        std::vector<int> bit(n + 1, 0);
        auto update = [&](int index, int value) {
            for (index++; index <= n; index += index & -index) bit[index] ^= value;
        };
        auto prefix = [&](int index) {
            int result = 0;
            for (; index > 0; index -= index & -index) result ^= bit[index];
            return result;
        };
        auto pathMask = [&](int u, int v) {
            int result = 0;
            while (head[u] != head[v]) {
                if (depth[head[u]] < depth[head[v]]) std::swap(u, v);
                result ^= prefix(position[u] + 1) ^ prefix(position[head[u]]);
                u = parent[head[u]];
            }
            if (position[u] > position[v]) std::swap(u, v);
            return result ^ prefix(position[v] + 1) ^ prefix(position[u]);
        };
        std::string current = s;
        for (int node = 0; node < n; node++) update(position[node], 1 << (current[node] - 'a'));
        std::vector<bool> answer;
        for (auto& query : queries) {
            std::istringstream iss(query);
            std::string op;
            int node;
            iss >> op >> node;
            if (op == "update") {
                std::string nc;
                iss >> nc;
                char newCharacter = nc[0];
                int delta = (1 << (current[node] - 'a')) ^ (1 << (newCharacter - 'a'));
                update(position[node], delta);
                current[node] = newCharacter;
            } else {
                int other;
                iss >> other;
                int mask = pathMask(node, other);
                answer.push_back((mask & (mask - 1)) == 0);
            }
        }
        return answer;
    }
};
