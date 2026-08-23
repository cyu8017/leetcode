// LeetCode 3922 - Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

var minFlips = function(s) {
    let ones = 0;
    for (const c of s) if (c === '1') ones++;
    let answer = ones;
    if (ones > 0) answer = ones - 1;
    const zeros = s.length - ones;
    answer = Math.min(answer, zeros);
    if (s.length >= 2) {
        let cost = 0;
        for (let i = 0; i < s.length; i++) {
            const want = (i === 0 || i === s.length - 1) ? '1' : '0';
            if (s[i] !== want) cost++;
        }
        answer = Math.min(answer, cost);
    }
    return answer;
};
