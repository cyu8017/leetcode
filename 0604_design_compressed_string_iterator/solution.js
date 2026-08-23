// LeetCode 0604 - Design Compressed String Iterator
// https://leetcode.com/problems/design-compressed-string-iterator/

/**
 * @param {string} compressedString
 */
var StringIterator = function(compressedString) {
    this.chars = [];
    this.counts = [];
    this.index = 0;
    let i = 0;
    const n = compressedString.length;
    while (i < n) {
        const ch = compressedString[i++];
        let j = i;
        while (j < n && compressedString[j] >= "0" && compressedString[j] <= "9") ++j;
        this.chars.push(ch);
        this.counts.push(Number(compressedString.substring(i, j)));
        i = j;
    }
};

/**
 * @return {character}
 */
StringIterator.prototype.next = function() {
    if (!this.hasNext()) return " ";
    const ch = this.chars[this.index];
    this.counts[this.index] -= 1;
    if (this.counts[this.index] === 0) ++this.index;
    return ch;
};

/**
 * @return {boolean}
 */
StringIterator.prototype.hasNext = function() {
    return this.index < this.chars.length;
};
