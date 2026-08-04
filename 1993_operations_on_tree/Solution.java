// LeetCode 1993 - Operations on Tree
// https://leetcode.com/problems/operations-on-tree/

import java.util.*;

class LockingTree {
    int[] locked;
    int[] parent;
    List<Integer>[] children;

    public LockingTree(int[] parent) {
        int n = parent.length;
        this.parent = parent;
        locked = new int[n];
        Arrays.fill(locked, -1);
        children = new ArrayList[n];
        for (int i = 0; i < n; i++) children[i] = new ArrayList<>();
        for (int son = 1; son < n; son++) children[parent[son]].add(son);
    }

    public boolean lock(int num, int user) {
        if (locked[num] == -1) {
            locked[num] = user;
            return true;
        }
        return false;
    }

    public boolean unlock(int num, int user) {
        if (locked[num] == user) {
            locked[num] = -1;
            return true;
        }
        return false;
    }

    public boolean upgrade(int num, int user) {
        int x = num;
        while (x != -1) {
            if (locked[x] != -1) return false;
            x = parent[x];
        }
        boolean[] find = {false};
        dfs(num, find);
        if (!find[0]) return false;
        locked[num] = user;
        return true;
    }

    private void dfs(int u, boolean[] find) {
        for (int v : children[u]) {
            if (locked[v] != -1) {
                locked[v] = -1;
                find[0] = true;
            }
            dfs(v, find);
        }
    }
}
