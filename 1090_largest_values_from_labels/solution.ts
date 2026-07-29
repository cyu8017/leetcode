// LeetCode 1090 - Largest Values From Labels
// https://leetcode.com/problems/largest-values-from-labels/

function largestValsFromLabels(values: number[], labels: number[], numWanted: number, useLimit: number): number {
    const items = values.map((v, i) => [v, labels[i]] as [number, number]).sort((a, b) => b[0] - a[0]);
    const used = new Map<number, number>();
    let ans = 0;
    let taken = 0;
    for (const [value, label] of items) {
        if (taken === numWanted) break;
        const cnt = used.get(label) || 0;
        if (cnt < useLimit) {
            used.set(label, cnt + 1);
            ans += value;
            taken++;
        }
    }
    return ans;
}
