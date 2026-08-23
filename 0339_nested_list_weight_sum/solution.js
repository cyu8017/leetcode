// LeetCode 0339 - Nested List Weight Sum
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
    let total = 0;

    const dfs = (items, depth) => {
        for (const item of items) {
            if (item.isInteger()) total += item.getInteger() * depth;
            else dfs(item.getList(), depth + 1);
        }
    };

    dfs(nestedList, 1);
    return total;
};
