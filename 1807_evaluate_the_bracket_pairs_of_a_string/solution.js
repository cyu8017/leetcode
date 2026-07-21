// LeetCode 1807 - Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

/**
 * @param {string} s
 * @param {string[][]} knowledge
 * @return {string}
 */
var evaluate = function(s, knowledge) {
    const lookup = new Map(knowledge);
    const result = [];
    let i = 0;
    while (i < s.length) {
        if (s[i] === '(') {
            const j = s.indexOf(')', i + 1);
            const key = s.slice(i + 1, j);
            result.push(lookup.has(key) ? lookup.get(key) : '?');
            i = j + 1;
        } else {
            result.push(s[i]);
            i += 1;
        }
    }
    return result.join('');
};
