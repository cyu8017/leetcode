// LeetCode 1803 - Count Pairs With XOR in a Range
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

/**
 * @param {number[]} nums
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countPairs = function(nums, low, high) {
    const MAX_BIT = 15;

    class TrieNode {
        constructor() {
            this.count = 0;
            this.children = [null, null];
        }
    }

    const insert = (root, num) => {
        let node = root;
        for (let i = MAX_BIT; i >= 0; i--) {
            const b = (num >> i) & 1;
            if (!node.children[b]) node.children[b] = new TrieNode();
            node = node.children[b];
            node.count += 1;
        }
    };

    const query = (root, num, limit, bit) => {
        if (!root || bit < 0) return 0;
        const numBit = (num >> bit) & 1;
        const limitBit = (limit >> bit) & 1;
        const child = root.children[numBit];
        if (limitBit === 1) {
            let result = child ? child.count : 0;
            result += query(root.children[1 - numBit], num, limit, bit - 1);
            return result;
        }
        return query(child, num, limit, bit - 1);
    };

    const countSmallerThan = (limit) => {
        if (limit <= 0) return 0;
        const root = new TrieNode();
        let total = 0;
        for (const num of nums) {
            total += query(root, num, limit, MAX_BIT);
            insert(root, num);
        }
        return total;
    };

    return countSmallerThan(high + 1) - countSmallerThan(low);
};
