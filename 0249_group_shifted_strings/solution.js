// LeetCode 0249 - Group Shifted Strings
// https://leetcode.com/problems/group-shifted-strings/

/**
 * @param {string[]} strings
 * @return {string[][]}
 */
var groupStrings = function(strings) {
    const groups = new Map();
    for (const text of strings) {
        let key;
        if (!text) {
            key = "";
        } else {
            const base = text.charCodeAt(0);
            key = [...text].map((char) => (char.charCodeAt(0) - base + 26) % 26).join(",");
        }
        if (!groups.has(key)) {
            groups.set(key, []);
        }
        groups.get(key).push(text);
    }
    return [...groups.values()];
};
