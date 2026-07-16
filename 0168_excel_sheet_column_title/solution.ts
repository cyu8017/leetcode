// LeetCode 0168 - Excel Sheet Column Title
// https://leetcode.com/problems/excel-sheet-column-title/

export function convertToTitle(columnNumber: number): string {
    const characters: string[] = [];
    while (columnNumber > 0) {
        columnNumber--;
        characters.push(String.fromCharCode('A'.charCodeAt(0) + (columnNumber % 26)));
        columnNumber = Math.floor(columnNumber / 26);
    }
    return characters.reverse().join('');
}