// LeetCode 3913 - Sort Vowels By Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/

export function sortVowels(s: any): any {
    const st = new Set(['a', 'e', 'i', 'o', 'u']);
    const vowels = [];
    const cnt = new Map();
    for (const c of s) {
        if (!st.has(c)) continue;
        if (!cnt.has(c)) { vowels.push(c); cnt.set(c, 0); }
        cnt.set(c, cnt.get(c) + 1);
    }
    vowels.sort((a, b) => cnt.get(b) - cnt.get(a));
    const ans = s.split('');
    let i = 0;
    for (let k = 0; k < s.length; k++) {
        if (!st.has(s[k])) continue;
        const ch = vowels[i];
        ans[k] = ch;
        cnt.set(ch, cnt.get(ch) - 1);
        if (cnt.get(ch) === 0) i++;
    }
    return ans.join('');
}
