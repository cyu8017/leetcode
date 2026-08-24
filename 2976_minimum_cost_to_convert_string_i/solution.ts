// LeetCode 2976 - Minimum Cost to Convert String I
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/

export function minimumCost(source: any, target: any, original: any, changed: any, cost: any): any {
    const inf = Number.MAX_SAFE_INTEGER / 4;
    const dist = Array.from({length: 26}, () => new Array(26).fill(inf));
    for (let i = 0; i < 26; i++) dist[i][i] = 0;
    for (let i = 0; i < original.length; i++) {
        const u = original[i].charCodeAt(0) - 97;
        const v = changed[i].charCodeAt(0) - 97;
        const ww = cost[i];
        if (ww < dist[u][v]) dist[u][v] = ww;
    }
    for (let k = 0; k < 26; k++)
        for (let i = 0; i < 26; i++)
            for (let j = 0; j < 26; j++)
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
    let ans = 0;
    for (let i = 0; i < source.length; i++) {
        const a = source.charCodeAt(i) - 97, b = target.charCodeAt(i) - 97;
        if (dist[a][b] >= inf / 2) return -1;
        ans += dist[a][b];
    }
    return ans;
}
