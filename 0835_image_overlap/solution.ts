// LeetCode 0835 - Image Overlap
// https://leetcode.com/problems/image-overlap/

export function largestOverlap(img1: number[][], img2: number[][]): number {
    const n = img1.length;
    const ones1 = [], ones2 = [];
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (img1[i][j] === 1) ones1.push([i, j]);
            if (img2[i][j] === 1) ones2.push([i, j]);
        }
    }
    if (!ones1.length || !ones2.length) return 0;
    const shifts = new Map();
    let best = 0;
    for (const [a0, a1] of ones1) {
        for (const [b0, b1] of ones2) {
            const key = ((a0 - b0 + n) << 16) | (a1 - b1 + n);
            const v = (shifts.get(key) || 0) + 1;
            shifts.set(key, v);
            best = Math.max(best, v);
        }
    }
    return best;
}
