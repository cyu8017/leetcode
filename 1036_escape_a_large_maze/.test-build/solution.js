"use strict";
// LeetCode 1036 - Escape a Large Maze
// https://leetcode.com/problems/escape-a-large-maze/
function isEscapePossible(blocked, source, target) {
    const blockedSet = new Set(blocked.map(([r, c]) => `${r},${c}`));
    const limit = blocked.length * (blocked.length - 1) / 2;
    const bfs = (start, goal) => {
        const queue = [[start[0], start[1]]];
        const seen = new Set([`${start[0]},${start[1]}`]);
        let qi = 0;
        while (qi < queue.length) {
            if (seen.size > limit)
                return true;
            const [r, c] = queue[qi++];
            if (r === goal[0] && c === goal[1])
                return true;
            for (const [nr, nc] of [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]) {
                const k = `${nr},${nc}`;
                if (nr >= 0 && nr < 1e6 && nc >= 0 && nc < 1e6 && !blockedSet.has(k) && !seen.has(k)) {
                    seen.add(k);
                    queue.push([nr, nc]);
                }
            }
        }
        return false;
    };
    return bfs(source, target) && bfs(target, source);
}
