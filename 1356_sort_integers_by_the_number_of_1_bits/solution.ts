// LeetCode 1356 - Sort Integers By The Number Of 1 Bits
// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

function sortByBits(arr: number[]): number[] {
    const bitCount = (x: any): any => {
        let c = 0;
        while (x) {
            c += x & 1;
            x >>= 1;
        }
        return c;
    };
    return [...arr].sort((a, b: any): any => bitCount(a) - bitCount(b) || a - b);
}
