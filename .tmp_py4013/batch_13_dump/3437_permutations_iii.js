// LeetCode 3437 - Permutations III
// https://leetcode.com/problems/permutations-iii/

var permute = function(n) {
    const ans = [];
    const used = new Array(n + 1).fill(false);
    const cur = [];
    const dfs = () => {
        if (cur.length === n) {
            ans.push(cur.slice());
            return;
        }
        for (let i = 1; i <= n; i++) {
            if (used[i]) continue;
            if (cur.length && (cur[cur.length - 1] % 2 === i % 2)) continue;
            used[i] = true;
            cur.push(i);
            dfs();
            cur.pop();
            used[i] = false;
        }
    };
    dfs();
    return ans;
};
