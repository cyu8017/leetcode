// LeetCode 2273 - Find Resultant Array After Removing Anagrams
// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

var removeAnagrams = function(words) {
    const sig = (w) => {
        const c = new Array(26).fill(0);
        for (const ch of w) c[ch.charCodeAt(0) - 97]++;
        return c;
    };
    const eq = (a, b) => {
        for (let i = 0; i < 26; i++) if (a[i] !== b[i]) return false;
        return true;
    };
    const ans = [words[0]];
    let prev = sig(words[0]);
    for (let i = 1; i < words.length; i++) {
        const cur = sig(words[i]);
        if (!eq(cur, prev)) {
            ans.push(words[i]);
            prev = cur;
        }
    }
    return ans;
};
