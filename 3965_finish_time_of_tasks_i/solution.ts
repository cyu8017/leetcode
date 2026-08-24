// LeetCode 3965 - Finish Time Of Tasks I
// https://leetcode.com/problems/finish-time-of-tasks-i/

export function finishTime(n: any, edges: any, baseTime: any): any {
        this.baseTime = baseTime;
        g = Array.from({length: n}, () => []);
        for (let i = 0; i < n; i++) g[i] = [];
        for (const e of edges) g[e[0]].push(e[1]);
        return dfs(0);
    
}export function dfs(i: any): any {
        if (g[i].length === 0) return baseTime[i];
        let INF = 1 << 62;
        let earliest = INF, latest = -INF;
        for (const j of g[i]) {
            let a = dfs(j);
            earliest = Math.min(earliest, a);
            latest = Math.max(latest, a);
        }
        let ownDuration = (latest - earliest) + baseTime[i];
        return latest + ownDuration;
    
}
