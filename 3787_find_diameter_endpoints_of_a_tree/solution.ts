// LeetCode 3787 - Find Diameter Endpoints Of A Tree
// https://leetcode.com/problems/find_diameter_endpoints_of_a_tree/

export function findSpecialNodes(n: any, edges: any): any {
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    const bfs = (start) => {
        const dist = new Array(n).fill(-1);
        dist[start] = 0;
        const q = [start];
        let far = start;
        for (let head = 0; head < q.length; head++) {
            const u = q[head];
            if (dist[u] > dist[far]) far = u;
            for (const v of g[u]) {
                if (dist[v] === -1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }
        return [far, dist];
    };
    const [a] = bfs(0);
    const [b, dist1] = bfs(a);
    const [, dist2] = bfs(b);
    const d = dist1[b];
    const ans = new Array(n).fill('0');
    for (let i = 0; i < n; i++) {
        if (dist1[i] === d || dist2[i] === d) ans[i] = '1';
    }
    return ans.join('');
}
