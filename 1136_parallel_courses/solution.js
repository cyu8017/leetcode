// LeetCode 1136 - Parallel Courses
// https://leetcode.com/problems/parallel-courses/

/**
 * @param {number} n
 * @param {number[][]} relations
 * @return {number}
 */
var minimumSemesters = function(n, relations) {
    const graph = Array.from({ length: n + 1 }, () => []);
    const indegree = Array(n + 1).fill(0);
    for (const [prev, nxt] of relations) {
        graph[prev].push(nxt);
        indegree[nxt]++;
    }
    const queue = [];
    for (let i = 1; i <= n; i++) if (indegree[i] === 0) queue.push(i);
    let semesters = 0, taken = 0, qi = 0;
    while (qi < queue.length) {
        const size = queue.length - qi;
        semesters++;
        for (let s = 0; s < size; s++) {
            const course = queue[qi++];
            taken++;
            for (const nxt of graph[course]) {
                indegree[nxt]--;
                if (indegree[nxt] === 0) queue.push(nxt);
            }
        }
    }
    return taken === n ? semesters : -1;
};
