class NestedInteger {
    private _integer: number | null;
    private _list: NestedInteger[] | null;

    constructor(value?: number | NestedInteger[]) {
        if (typeof value === "number") {
            this._integer = value;
            this._list = null;
        } else {
            this._integer = null;
            this._list = value ?? [];
        }
    }

    isInteger(): boolean {
        return this._integer !== null;
    }

    getInteger(): number {
        return this._integer ?? 0;
    }

    getList(): NestedInteger[] {
        return this._list ?? [];
    }
}

export class NestedIterator {
    private stack: Array<[NestedInteger, number]>;

    constructor(nestedList: NestedInteger[]) {
        this.stack = [];
        for (let index = nestedList.length - 1; index >= 0; index -= 1) {
            this.stack.push([nestedList[index], 0]);
        }
    }

    private prepareNext(): void {
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

    next(): number {
        this.prepareNext();
        const [current] = this.stack.pop()!;
        return current.getInteger();
    }

    hasNext(): boolean {
        this.prepareNext();
        return this.stack.length > 0;
    }
}
