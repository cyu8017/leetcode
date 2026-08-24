// LeetCode 2325 - Decode the Message
// https://leetcode.com/problems/decode-the-message/

/**
 * @param {string} key
 * @param {string} message
 * @return {string}
 */
var decodeMessage = function(key, message) {
    const mp = Array(26).fill(0);
    let next = 97;
    for (const c of key) {
        if (c === ' ' || mp[c.charCodeAt(0) - 97] !== 0) continue;
        mp[c.charCodeAt(0) - 97] = next++;
    }
    const outc = message.split('');
    for (let i = 0; i < outc.length; i++) {
        if (outc[i] !== ' ') outc[i] = String.fromCharCode(mp[outc[i].charCodeAt(0) - 97]);
    }
    return outc.join('');
};
