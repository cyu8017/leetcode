// LeetCode 0247 - Strobogrammatic Number II
// https://leetcode.com/problems/strobogrammatic-number-ii/

export function findStrobogrammatic(n: number): string[] {
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

    return build(0, n - 1);
}
