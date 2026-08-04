// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

function buildCombinations(characters, k, start, path, depth, out) {
    if (depth === k) {
        out.push(path.join(''));
        return;
    }
    for (let i = start; i < characters.length; i++) {
        path[depth] = characters[i];
        buildCombinations(characters, k, i + 1, path, depth + 1, out);
    }
}

/**
 * @param {string} characters
 * @param {number} combinationLength
 */
var CombinationIterator = function(characters, combinationLength) {
    this.items = [];
    buildCombinations(characters, combinationLength, 0, new Array(combinationLength), 0, this.items);
    this.index = 0;
};

/**
 * @return {string}
 */
CombinationIterator.prototype.next = function() {
    return this.items[this.index++];
};

/**
 * @return {boolean}
 */
CombinationIterator.prototype.hasNext = function() {
    return this.index < this.items.length;
};
