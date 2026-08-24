// LeetCode 2027 - Minimum Moves to Convert String
// https://leetcode.com/problems/minimum-moves-to-convert-string/

export function minimumMoves(s: string): number {
    let ans = 0;
    for (let i = 0; i < s.length; ) {
        if (s[i] === 'X') { ans++; i += 3; }
        else i++;
    }
    return ans;
}
