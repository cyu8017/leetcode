// LeetCode 0171 - Excel Sheet Column Number
// https://leetcode.com/problems/excel-sheet-column-number/

export function titleToNumber(columnTitle: string): number {
    let result = 0;
    for (const char of columnTitle) {
        result = result * 26 + char.charCodeAt(0) - "A".charCodeAt(0) + 1;
    }
    return result;
}