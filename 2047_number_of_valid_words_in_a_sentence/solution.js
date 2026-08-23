// LeetCode 2047 - Number of Valid Words in a Sentence
// https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

/**
 * @param {string} sentence
 * @return {number}
 */
var countValidWords = function(sentence) {
    const valid = (w) => {
        if (w.length === 0) return false;
        let hyphen = 0;
        for (let i = 0; i < w.length; i++) {
            const c = w[i];
            if (c >= '0' && c <= '9') return false;
            if (c === '-') {
                hyphen++;
                if (hyphen > 1 || i === 0 || i === w.length - 1) return false;
                if (w[i - 1] < 'a' || w[i - 1] > 'z' || w[i + 1] < 'a' || w[i + 1] > 'z') return false;
            } else if (c === '!' || c === '.' || c === ',') {
                if (i !== w.length - 1) return false;
            } else if (c < 'a' || c > 'z') return false;
        }
        return true;
    };
    let ans = 0;
    for (const tok of sentence.split(" "))
        if (valid(tok)) ans++;
    return ans;
};
