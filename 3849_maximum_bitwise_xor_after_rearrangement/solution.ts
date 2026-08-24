// LeetCode 3849 - Maximum Bitwise Xor After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

export function maximumXor(s: any, t: any): any {
    const cnt = [0, 0];
    for (const c of t) cnt[c.charCodeAt(0) - 48]++;
    const ans = new Array(s.length);
    for (let i = 0; i < s.length; i++) {
        const x = s.charCodeAt(i) - 48;
        if (cnt[x ^ 1] > 0) {
            cnt[x ^ 1]--;
            ans[i] = '1';
        } else {
            cnt[x]--;
            ans[i] = '0';
        }
    }
    return ans.join('');
}
