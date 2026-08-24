// LeetCode 2076 - Process Restricted Friend Requests
// https://leetcode.com/problems/process-restricted-friend-requests/

export function friendRequests(n: number, restrictions: number[][], requests: number[][]): boolean[] {
    const parent = Array.from({length: n}, (_, i) => i);
    const find = (x) => parent[x] === x ? x : (parent[x] = find(parent[x]));
    const unite = (a, b) => {
        a = find(a); b = find(b);
        if (a !== b) parent[a] = b;
    };
    const ans = new Array(requests.length);
    for (let i = 0; i < requests.length; i++) {
        const u = find(requests[i][0]), v = find(requests[i][1]);
        let ok = true;
        if (u !== v) {
            for (const r of restrictions) {
                const x = find(r[0]), y = find(r[1]);
                if ((x === u && y === v) || (x === v && y === u)) { ok = false; break; }
            }
        }
        ans[i] = ok;
        if (ok) unite(u, v);
    }
    return ans;
}
