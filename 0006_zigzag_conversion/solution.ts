// LeetCode 0006 - Zigzag Conversion
// https://leetcode.com/problems/zigzag-conversion/

export function convert(s: string, numRows: number): string {
    if (numRows === 1 || numRows >= s.length) {
        return s;
    }

    const rows: string[][] = Array.from({ length: numRows }, () => []);
    let index = 0;
    let step = 1;

    for (const ch of s) {
        rows[index].push(ch);
        if (index === 0) {
            step = 1;
        } else if (index === numRows - 1) {
            step = -1;
        }
        index += step;
    }

    return rows.map((row) => row.join("")).join("");
}
