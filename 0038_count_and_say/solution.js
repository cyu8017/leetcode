// LeetCode 0038 - Count and Say
// https://leetcode.com/problems/count-and-say/

/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    let term = "1";

    for (let i = 1; i < n; i++) {
        const nextTerm = [];
        let index = 0;
        while (index < term.length) {
            let count = 1;
            while (index + count < term.length && term[index + count] === term[index]) {
                count++;
            }
            nextTerm.push(String(count));
            nextTerm.push(term[index]);
            index += count;
        }
        term = nextTerm.join("");
    }

    return term;
};
