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
    const weighted: Array<[number, number]> = [];

    const dfs = (items: NestedInteger[], depth: number): void => {
        for (const item of items) {
            if (item.isInteger()) weighted.push([item.getInteger(), depth]);
            else dfs(item.getList(), depth + 1);
        }
    };

    dfs(nestedList, 1);
    if (!weighted.length) return 0;

    const maxDepth = Math.max(...weighted.map(([, depth]) => depth));
    return weighted.reduce((sum, [value, depth]) => sum + value * (maxDepth - depth + 1), 0);
}
