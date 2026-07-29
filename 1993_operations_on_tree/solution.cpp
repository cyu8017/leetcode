// LeetCode 1993 - Operations on Tree
#include <functional>
#include <vector>

class LockingTree {
    std::vector<int> locked, parent;
    std::vector<std::vector<int>> children;
public:
    LockingTree(std::vector<int>& parent) : locked(parent.size(), -1), parent(parent), children(parent.size()) {
        for (int son = 1; son < (int)parent.size(); son++) children[parent[son]].push_back(son);
    }
    bool lock(int num, int user) {
        if (locked[num] == -1) { locked[num] = user; return true; }
        return false;
    }
    bool unlock(int num, int user) {
        if (locked[num] == user) { locked[num] = -1; return true; }
        return false;
    }
    bool upgrade(int num, int user) {
        int x = num;
        while (x != -1) {
            if (locked[x] != -1) return false;
            x = parent[x];
        }
        bool find = false;
        std::function<void(int)> dfs = [&](int u) {
            for (int v : children[u]) {
                if (locked[v] != -1) { locked[v] = -1; find = true; }
                dfs(v);
            }
        };
        dfs(num);
        if (!find) return false;
        locked[num] = user;
        return true;
    }
};
