// LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

/**
 * @param {string} s
 * @return {number}
 */
var minFlips = function(s) {
    const n = s.length;
    const doubled = s + s;
    let alt0 = 0, alt1 = 0;
    for (let i = 0; i < n; i++) {
        if (doubled[i] !== (i % 2 === 0 ? "0" : "1")) alt0++;
        if (doubled[i] !== (i % 2 === 0 ? "1" : "0")) alt1++;
    }
    let answer = Math.min(alt0, alt1);
    for (let i = 0; i < n; i++) {
        if (doubled[i] !== (i % 2 === 0 ? "0" : "1")) alt0--;
        if (doubled[i + n] !== ((i + n) % 2 === 0 ? "0" : "1")) alt0++;
        if (doubled[i] !== (i % 2 === 0 ? "1" : "0")) alt1--;
        if (doubled[i + n] !== ((i + n) % 2 === 0 ? "1" : "0")) alt1++;
        answer = Math.min(answer, alt0, alt1);
    }
    return answer;
};
