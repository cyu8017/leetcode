// LeetCode 0809 - Expressive Words
// https://leetcode.com/problems/expressive-words/

/**
 * @param {string} s
 * @param {string[]} words
 * @return {number}
 */
var expressiveWords = function(s, words) {
    const groups = (text) => {
        const result = [];
        let i = 0, n = text.length;
        while (i < n) {
            let j = i;
            while (j < n && text[j] === text[i]) j++;
            result.push([text.charCodeAt(i), j - i]);
            i = j;
        }
        return result;
    };
    const target = groups(s);
    let ans = 0;
    for (const word of words) {
        const source = groups(word);
        if (source.length !== target.length) continue;
        let ok = true;
        for (let i = 0; i < source.length; i++) {
            if (source[i][0] !== target[i][0]) { ok = false; break; }
            const c1 = source[i][1], c2 = target[i][1];
            if (c1 > c2 || (c1 !== c2 && c2 < 3)) { ok = false; break; }
        }
        if (ok) ans++;
    }
    return ans;
};
