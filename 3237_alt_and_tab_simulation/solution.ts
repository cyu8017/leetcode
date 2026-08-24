// LeetCode 3237 - Alt and Tab Simulation
// https://leetcode.com/problems/alt-and-tab-simulation/

export function simulationResult(windows: any, queries: any): any {
    const n = windows.length;
    const s = new Array(n + 1).fill(false);
    const ans = [];
    for (let i = queries.length - 1; i >= 0; i--) {
        const q = queries[i];
        if (!s[q]) { s[q] = true; ans.push(q); }
    }
    for (const w of windows) if (!s[w]) ans.push(w);
    return ans;
}
