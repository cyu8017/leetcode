// LeetCode 0364 - Nested List Weight Sum II
class NestedInteger {
    constructor(value) {
        if (typeof value === "number") {
            this._integer = value;
            this._list = null;
        } else {
            this._integer = null;
            this._list = value || [];
        }
    }

    isInteger() {
        return this._integer !== null;
    }

    getInteger() {
        return this._integer ?? 0;
    }

    getList() {
        return this._list ?? [];
    }
}

var depthSum = function(nestedList) {
    const weighted = [];

    const dfs = (items, depth) => {
        for (const item of items) {
            if (item.isInteger()) weighted.push([item.getInteger(), depth]);
            else dfs(item.getList(), depth + 1);
        }
    };

    dfs(nestedList, 1);
    if (!weighted.length) return 0;

    const maxDepth = Math.max(...weighted.map(([, depth]) => depth));
    return weighted.reduce((sum, [value, depth]) => sum + value * (maxDepth - depth + 1), 0);
};
