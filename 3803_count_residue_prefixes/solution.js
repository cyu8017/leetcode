// LeetCode 3803 - Count Residue Prefixes
// https://leetcode.com/problems/count-residue-prefixes/

var residuePrefixes = function(s) {
    const st = new Set();
    let ans = 0;
    for (let i = 0; i < s.length; i++) {
        st.add(s[i]);
        if (st.size === (i + 1) % 3) ans++;
    }
    return ans;
};
