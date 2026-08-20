// LeetCode 1993 - Operations on Tree
// https://leetcode.com/problems/operations-on-tree/

class LockingTree {
    locked: number[];
    parent: number[];
    children: number[][];

    constructor(parent: number[]) {
        const n = parent.length;
        this.locked = new Array(n).fill(-1);
        this.parent = parent;
        this.children = Array.from({ length: n }, () => [] as number[]);
        for (let son = 1; son < n; son++) this.children[parent[son]].push(son);
    }

    lock(num: number, user: number): boolean {
        if (this.locked[num] === -1) {
            this.locked[num] = user;
            return true;
        }
        return false;
    }

    unlock(num: number, user: number): boolean {
        if (this.locked[num] === user) {
            this.locked[num] = -1;
            return true;
        }
        return false;
    }

    upgrade(num: number, user: number): boolean {
        let x = num;
        while (x !== -1) {
            if (this.locked[x] !== -1) return false;
            x = this.parent[x];
        }
        let find = false;
        const dfs = (u: number): void => {
            for (const v of this.children[u]) {
                if (this.locked[v] !== -1) {
                    this.locked[v] = -1;
                    find = true;
                }
                dfs(v);
            }
        };
        dfs(num);
        if (!find) return false;
        this.locked[num] = user;
        return true;
    }
}
