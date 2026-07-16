// LeetCode 0248 - Strobogrammatic Number III
// https://leetcode.com/problems/strobogrammatic-number-iii/

export function strobogrammaticInRange(low: string, high: string): number {
    const pairs: [string, string][] = [
        ["0", "0"],
        ["1", "1"],
        ["6", "9"],
        ["8", "8"],
        ["9", "6"],
    ];

    const build = (left: number, right: number): string[] => {
        if (left > right) {
            return [""];
        }
        if (left === right) {
            return ["0", "1", "8"];
        }
        const result: string[] = [];
        for (const [start, end] of pairs) {
            if (left === 0 && start === "0") {
                continue;
            }
            for (const middle of build(left + 1, right - 1)) {
                result.push(start + middle + end);
            }
        }
        return result;
    };

    const lowValue = Number(low);
    const highValue = Number(high);
    let count = 0;
    for (let length = low.length; length <= high.length; length++) {
        for (const value of build(0, length - 1)) {
            const numeric = Number(value);
            if (lowValue <= numeric && numeric <= highValue) {
                count += 1;
            }
        }
    }
    return count;
}
