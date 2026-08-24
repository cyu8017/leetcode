// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically_smallest_permutation_greater_than_target/

export function lexGreaterPermutation(s: any, target: any): any {
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    const n = s.length;
    const ans = new Array(n);
    const dfs = (pos, greater) => {
        if (pos === n) return greater;
        const start = greater ? 0 : (target.charCodeAt(pos) - 97);
        for (let c = start; c < 26; c++) {
            if (cnt[c] === 0) continue;
            cnt[c]--;
            ans[pos] = String.fromCharCode(97 + c);
            const ng = greater || c > (target.charCodeAt(pos) - 97);
            if (dfs(pos + 1, ng)) return true;
            cnt[c]++;
        }
        return false;
    };
    if (dfs(0, false)) return ans.join('');
    return "";
}
