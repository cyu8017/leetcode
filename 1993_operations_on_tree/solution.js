// LeetCode 1993 - Operations on Tree
// https://leetcode.com/problems/operations-on-tree/

class LockingTree {
    /**
     * @param {number[]} parent
     */
    constructor(parent) {
        const n = parent.length;
        this.locked = new Array(n).fill(-1);
        this.parent = parent;
        this.children = Array.from({ length: n }, () => []);
        for (let son = 1; son < n; son++) this.children[parent[son]].push(son);
    }

    /**
     * @param {number} num
     * @param {number} user
     * @return {boolean}
     */
    lock(num, user) {
        if (this.locked[num] === -1) {
            this.locked[num] = user;
            return true;
        }
        return false;
    }

    /**
     * @param {number} num
     * @param {number} user
     * @return {boolean}
     */
    unlock(num, user) {
        if (this.locked[num] === user) {
            this.locked[num] = -1;
            return true;
        }
        return false;
    }

    /**
     * @param {number} num
     * @param {number} user
     * @return {boolean}
     */
    upgrade(num, user) {
        let x = num;
        while (x !== -1) {
            if (this.locked[x] !== -1) return false;
            x = this.parent[x];
        }
        let find = false;
        const dfs = (u) => {
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

module.exports = { LockingTree };
