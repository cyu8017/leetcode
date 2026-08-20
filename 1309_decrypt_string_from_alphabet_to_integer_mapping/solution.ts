// LeetCode 1309 - Decrypt String From Alphabet To Integer Mapping
// https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

function freqAlphabets(s: string): string {
    const answer: any[] = [];
    let i = s.length - 1;
    while (i >= 0) {
        if (s[i] === "#") {
            answer.push(String.fromCharCode(96 + Number(s.slice(i - 2, i))));
            i -= 3;
        } else {
            answer.push(String.fromCharCode(96 + Number(s[i])));
            i -= 1;
        }
    }
    return answer.reverse().join("");
}
