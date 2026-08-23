// LeetCode 0318 - Maximum Product of Word Lengths
// https://leetcode.com/problems/maximum-product-of-word-lengths/

/**
 * @param {string[]} words
 * @return {number}
 */
var maxProduct = function(words) {
    const masks = [];
    const lengths = [];
    for (const word of words) {
        let mask = 0;
        let valid = true;
        for (const char of word) {
            const bit = 1 << (char.charCodeAt(0) - 97);
            if (mask & bit) {
                valid = false;
                break;
            }
            mask |= bit;
        }
        masks.push(valid ? mask : 0);
        lengths.push(word.length);
    }
    let best = 0;
    for (let left = 0; left < words.length; left += 1) {
        if (masks[left] === 0) {
            continue;
        }
        for (let right = left + 1; right < words.length; right += 1) {
            if (masks[right] === 0) {
                continue;
            }
            if ((masks[left] & masks[right]) === 0) {
                best = Math.max(best, lengths[left] * lengths[right]);
            }
        }
    }
    return best;
};
