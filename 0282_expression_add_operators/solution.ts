// LeetCode 0282 - Expression Add Operators
// https://leetcode.com/problems/expression-add-operators/

export function addOperators(num: string, target: number): string[] {
    const result: string[] = [];

    function backtrack(index: number, path: string, value: number, previous: number): void {
        if (index === num.length) {
            if (value === target) {
                result.push(path);
            }
            return;
        }
        for (let end = index; end < num.length; end += 1) {
            if (end > index && num[index] === "0") {
                break;
            }
            const currentStr = num.slice(index, end + 1);
            const current = parseInt(currentStr, 10);
            if (index === 0) {
                backtrack(end + 1, currentStr, current, current);
            } else {
                backtrack(end + 1, path + "+" + currentStr, value + current, current);
                backtrack(end + 1, path + "-" + currentStr, value - current, -current);
                backtrack(end + 1, path + "*" + currentStr, value - previous + previous * current, previous * current);
            }
        }
    }

    backtrack(0, "", 0, 0);
    return result;
}
