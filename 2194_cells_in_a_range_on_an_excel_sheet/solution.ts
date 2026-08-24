// LeetCode 2194 - Cells in a Range on an Excel Sheet
// https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

export function cellsInRange(s: string): string[] {
    const ans = [];
    for (let c = s.charCodeAt(0); c <= s.charCodeAt(3); c++)
        for (let r = s.charCodeAt(1); r <= s.charCodeAt(4); r++)
            ans.push(String.fromCharCode(c) + String.fromCharCode(r));
    return ans;
}
