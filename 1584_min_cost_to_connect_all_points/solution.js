// LeetCode 1584 - Min Cost to Connect All Points
// https://leetcode.com/problems/min-cost-to-connect-all-points/

/**
 * @param {number[][]} points
 * @return {number}
 */
var minCostConnectPoints = function(points) {
    const n = points.length;
    const used = Array(n).fill(false);
    const dist = Array(n).fill(1e9);
    dist[0] = 0;
    let answer = 0;
    for (let t = 0; t < n; t++) {
        let u = -1;
        for (let i = 0; i < n; i++) {
            if (!used[i] && (u === -1 || dist[i] < dist[u])) u = i;
        }
        used[u] = true;
        answer += dist[u];
        for (let v = 0; v < n; v++) {
            if (!used[v]) {
                const d = Math.abs(points[u][0] - points[v][0]) + Math.abs(points[u][1] - points[v][1]);
                dist[v] = Math.min(dist[v], d);
            }
        }
    }
    return answer;
};
