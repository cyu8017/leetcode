// LeetCode 0271 - Encode and Decode Strings
// https://leetcode.com/problems/encode-and-decode-strings/

class Codec {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    encode(strs) {
        return strs.map((text) => `${text.length}#${text}`).join("");
    }

    /**
     * @param {string} encoded
     * @return {string[]}
     */
    decode(encoded) {
        const result = [];
        let index = 0;
        while (index < encoded.length) {
            const delimiter = encoded.indexOf("#", index);
            const length = parseInt(encoded.slice(index, delimiter), 10);
            const start = delimiter + 1;
            result.push(encoded.slice(start, start + length));
            index = start + length;
        }
        return result;
    }
}

/**
 * @param {string[]} strs
 * @return {string}
 */
function encode(strs) {
    return new Codec().encode(strs);
}

module.exports = { Codec };
