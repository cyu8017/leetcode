// LeetCode 1736 - Latest Time by Replacing Hidden Digits
// https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

function maximumTime(time: string): string {
    const chars = time.split("");
    if (chars[0] === "?") {
        chars[0] = "0123?".includes(chars[1]) ? "2" : "1";
    }
    if (chars[1] === "?") {
        chars[1] = chars[0] === "2" ? "3" : "9";
    }
    if (chars[3] === "?") {
        chars[3] = "5";
    }
    if (chars[4] === "?") {
        chars[4] = "9";
    }
    return chars.join("");
}
