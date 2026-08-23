// LeetCode 0797 - All Paths From Source to Target
// https://leetcode.com/problems/all-paths-from-source-to-target/

/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function(graph) {
    const target = graph.length - 1;
    const answer = [];
    const path = [0];
    const dfs = (node) => {
        if (node === target) {
            answer.push(path.slice());
            return;
        }
        for (const nei of graph[node]) {
            path.push(nei);
            dfs(nei);
            path.pop();
        }
    };
    dfs(0);
    return answer;
};
