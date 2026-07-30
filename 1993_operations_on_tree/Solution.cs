// LeetCode 1993 - Operations on Tree
// https://leetcode.com/problems/operations-on-tree/

using System.Collections.Generic;

public class LockingTree {
    int[] locked;
    int[] parent;
    List<int>[] children;

    public LockingTree(int[] parent) {
        int n = parent.Length;
        this.parent = parent;
        locked = new int[n];
        for (int i = 0; i < n; i++) locked[i] = -1;
        children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        for (int son = 1; son < n; son++) children[parent[son]].Add(son);
    }

    public bool Lock(int num, int user) {
        if (locked[num] == -1) { locked[num] = user; return true; }
        return false;
    }

    public bool Unlock(int num, int user) {
        if (locked[num] == user) { locked[num] = -1; return true; }
        return false;
    }

    public bool Upgrade(int num, int user) {
        int x = num;
        while (x != -1) {
            if (locked[x] != -1) return false;
            x = parent[x];
        }
        bool find = false;
        void Dfs(int u) {
            foreach (int v in children[u]) {
                if (locked[v] != -1) { locked[v] = -1; find = true; }
                Dfs(v);
            }
        }
        Dfs(num);
        if (!find) return false;
        locked[num] = user;
        return true;
    }
}