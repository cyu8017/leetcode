// LeetCode 3211 - Generate Binary Strings Without Adjacent Zeros
// https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

var validStrings = function(n) {
    const ans = [];
    const t = [];
    const dfs = (i) => {
        if (i >= n) { ans.push(t.join('')); return; }
        for (let j = 0; j < 2; j++) {
            if ((j === 0 && (i === 0 || t[i - 1] === '1')) || j === 1) {
                t.push(String(j));
                dfs(i + 1);
                t.pop();
            }
        }
    };
    dfs(0);
    return ans;
};
