// LeetCode 3805 - Count Caesar Cipher Pairs
// https://leetcode.com/problems/count-caesar-cipher-pairs/

export function countPairs(words: any): any {
    const cnt = new Map();
    for (const word of words) {
        const s = word.split('');
        const k = 'z'.charCodeAt(0) - s[0].charCodeAt(0);
        for (let i = 1; i < s.length; i++) {
            s[i] = String.fromCharCode(97 + (s[i].charCodeAt(0) - 97 + k) % 26);
        }
        s[0] = 'z';
        const key = s.join('');
        cnt.set(key, (cnt.get(key) || 0) + 1);
    }
    let ans = 0;
    for (const v of cnt.values()) ans += v * (v - 1) / 2;
    return ans;
}
