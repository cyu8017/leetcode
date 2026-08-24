// LeetCode 2645 - Minimum Additions to Make Valid String
// https://leetcode.com/problems/minimum-additions-to-make-valid-string/

export function addMinimum(word: any): any {
    let ans = 0, expect = 0, i = 0, n = word.length;
    while (i < n) {
        const need = String.fromCharCode(97 + expect);
        if (word[i] === need) i++;
        else ans++;
        expect = (expect + 1) % 3;
    }
    ans += (3 - expect) % 3;
    return ans;
}
