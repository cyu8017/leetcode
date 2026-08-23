// LeetCode 0341 - Flatten Nested List Iterator
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

class NestedIterator {
    constructor(nestedList) {
        this.stack = [];
        for (let index = nestedList.length - 1; index >= 0; index -= 1) {
            this.stack.push([nestedList[index], 0]);
        }
    }

    _prepareNext() {
        while (this.stack.length) {
            const [current, childIndex] = this.stack[this.stack.length - 1];
            if (current.isInteger()) return;
            const nested = current.getList();
            if (childIndex >= nested.length) {
                this.stack.pop();
                continue;
            }
            this.stack[this.stack.length - 1] = [current, childIndex + 1];
            this.stack.push([nested[childIndex], 0]);
        }
    }

    next() {
        this._prepareNext();
        const [current] = this.stack.pop();
        return current.getInteger();
    }

    hasNext() {
        this._prepareNext();
        return this.stack.length > 0;
    }
}

module.exports = { NestedInteger, NestedIterator };
