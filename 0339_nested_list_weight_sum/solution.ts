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

export function depthSum(nestedList: NestedInteger[]): number {
    let total = 0;

    const dfs = (items: NestedInteger[], depth: number): void => {
        for (const item of items) {
            if (item.isInteger()) total += item.getInteger() * depth;
            else dfs(item.getList(), depth + 1);
        }
    };

    dfs(nestedList, 1);
    return total;
}
