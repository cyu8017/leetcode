// LeetCode 2947 - Count Beautiful Substrings I
// https://leetcode.com/problems/count-beautiful-substrings-i/

function isVowel(c: any): any {
    return c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u';
}export function beautifulSubstrings(s: any, k: any): any {
    let ans = 0;
    const n = s.length;
    for (let i = 0; i < n; i++) {
        let v = 0, c = 0;
        for (let j = i; j < n; j++) {
            if (isVowel(s[j])) v++;
            else c++;
            if (v === c && (v * c) % k === 0) ans++;
        }
    }
    return ans;
}
