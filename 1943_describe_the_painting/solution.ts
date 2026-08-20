// LeetCode 1943 - Describe the Painting
// https://leetcode.com/problems/describe-the-painting/

function splitPainting(segments: number[][]): number[][] {
    const diff = new Map();
    for (const [s, e, c] of segments) {
        diff.set(s, (diff.get(s) || 0) + c);
        diff.set(e, (diff.get(e) || 0) - c);
    }
    const points = [...diff.keys()].sort((a, b: any) => a - b);
    const ans = [];
    let cur = 0;
    for (let i = 0; i < points.length - 1; i++) {
        cur += diff.get(points[i]);
        if (cur) ans.push([points[i], points[i + 1], cur]);
    }
    return ans;
}
