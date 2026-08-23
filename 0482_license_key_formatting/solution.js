// LeetCode 0482 - License Key Formatting
// https://leetcode.com/problems/license-key-formatting/

class Solution {
    licenseKeyFormatting(s, k) {
        const chars = [...s].filter((ch) => ch !== "-").map((ch) => ch.toUpperCase());
        if (chars.length === 0) return "";
        const firstLen = chars.length % k || k;
        const parts = [chars.slice(0, firstLen).join("")];
        for (let index = firstLen; index < chars.length; index += k) {
            parts.push(chars.slice(index, index + k).join(""));
        }
        return parts.join("-");
    }
}

module.exports = { Solution };
