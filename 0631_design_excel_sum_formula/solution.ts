// LeetCode 0631 - Design Excel Sum Formula
// https://leetcode.com/problems/design-excel-sum-formula/

export class Excel {
    constructor(height: number, width: string) {
    this.values = Array.from({ length: height + 1 }, () => Array(width.charCodeAt(0) - 64).fill(0));
    this.formulas = new Map();
}
    set(row: number, column: string, val: number): void {
    const col = column.charCodeAt(0) - 65;
    this.formulas.delete(this._key(row, col).toString());
    this.values[row][col] = val;
}
    get(row: number, column: string): number {
    return this._eval(row, column.charCodeAt(0) - 65);
}
    sum(row: number, column: string, numbers: string[]): number {
    const col = column.charCodeAt(0) - 65;
    const cells = [];
    for (const token of numbers) {
        const colon = token.indexOf(":");
        if (colon >= 0) {
            const p1 = this._parse(token.substring(0, colon));
            const p2 = this._parse(token.substring(colon + 1));
            for (let r = p1[0]; r <= p2[0]; ++r) {
                for (let c = p1[1]; c <= p2[1]; ++c) cells.push([r, c]);
            }
        } else {
            cells.push(this._parse(token));
        }
    }
    this.formulas.set(this._key(row, col).toString(), cells);
    return this._eval(row, col);
}
}
