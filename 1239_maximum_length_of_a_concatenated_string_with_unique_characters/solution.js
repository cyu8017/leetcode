// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

/**
 * @param {string[]} arr
 * @return {number}
 */
var maxLength = function(arr) {
    let masks = [[0, 0]];
    for (const word of arr) {
        let mask = 0;
        for (const ch of word) mask |= 1 << (ch.charCodeAt(0) - 97);
        if (popcount(mask) !== word.length) continue;
        masks = masks.concat(
            masks
                .filter(([used]) => !(used & mask))
                .map(([used, length]) => [used | mask, length + word.length])
        );
    }
    return Math.max(...masks.map(([, length]) => length));
};

function popcount(x) {
    let count = 0;
    while (x) {
        count += x & 1;
        x >>= 1;
    }
    return count;
}
