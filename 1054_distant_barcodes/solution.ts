// LeetCode 1054 - Distant Barcodes
// https://leetcode.com/problems/distant-barcodes/

function rearrangeBarcodes(barcodes: number[]): number[] {
    const count = new Map<number, number>();
    for (const x of barcodes) count.set(x, (count.get(x) || 0) + 1);
    const items = [...count.entries()].sort((a, b) => b[1] - a[1]);
    const n = barcodes.length;
    const ans = new Array<number>(n);
    let i = 0;
    for (const [value, freq] of items) {
        for (let k = 0; k < freq; k++) {
            ans[i] = value;
            i += 2;
            if (i >= n) i = 1;
        }
    }
    return ans;
}
