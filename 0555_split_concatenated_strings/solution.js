// LeetCode 0555 - Split Concatenated Strings
// https://leetcode.com/problems/split-concatenated-strings/

/**
 * @param {string[]} strs
 * @return {string}
 */
var splitLoopedString = function(strs) {
    const bestForms = new Array(strs.length);
    for (let i = 0; i < strs.length; ++i) {
        const s = strs[i];
        const rev = s.split("").reverse().join("");
        bestForms[i] = s >= rev ? s : rev;
    }
    let answer = "";
    for (let i = 0; i < strs.length; ++i) {
        let mid = "";
        for (let j = i + 1; j < strs.length; ++j) mid += bestForms[j];
        for (let j = 0; j < i; ++j) mid += bestForms[j];
        const candidates = [strs[i], strs[i].split("").reverse().join("")];
        for (const candidate of candidates) {
            for (let cut = 0; cut < candidate.length; ++cut) {
                const formed = candidate.substring(cut) + mid + candidate.substring(0, cut);
                if (formed > answer) answer = formed;
            }
        }
    }
    return answer;
};
