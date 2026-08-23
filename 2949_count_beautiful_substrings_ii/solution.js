// LeetCode 2949 - Count Beautiful Substrings II
// https://leetcode.com/problems/count-beautiful-substrings-ii/

function isVowel(c) {
    return c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u';
}
var beautifulSubstrings = function(s, k) {
    let x = 1;
    while ((x * x) % k !== 0) x++;
    const freq = new Map();
    freq.set(0, 1);
    let bal = 0, vowels = 0, ans = 0;
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (isVowel(ch)) { bal++; vowels++; }
        else bal--;
        const kk = (BigInt(bal) << 32n) | BigInt(vowels % x);
        const key = kk.toString();
        const f = freq.get(key) || 0;
        ans += f;
        freq.set(key, f + 1);
    }
    return ans;
};
