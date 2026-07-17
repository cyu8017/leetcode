// LeetCode 1796 - Second Largest Digit in a String
// https://leetcode.com/problems/second-largest-digit-in-a-string/

function secondHighest(s: string): number {
    let largest = -1;
    let second = -1;
    for (const ch of s) {
        if (ch >= '0' && ch <= '9') {
            const d = ch.charCodeAt(0) - 48;
            if (d > largest) {
                second = largest;
                largest = d;
            } else if (d < largest && d > second) {
                second = d;
            }
        }
    }
    return second;
}
