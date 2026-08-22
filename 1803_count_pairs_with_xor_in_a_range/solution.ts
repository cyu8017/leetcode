// LeetCode 1803 - Count Pairs With XOR in a Range
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

function countPairs(nums: number[], low: number, high: number): number {
    const MAX_BIT = 15;

    class TrieNode {
        count = 0;
        children: (TrieNode | null)[] = [null, null];
    }

    const insert = (root: TrieNode, num: number): void => {
        let node = root;
        for (let i = MAX_BIT; i >= 0; i--) {
            const b = (num >> i) & 1;
            if (!node.children[b]) node.children[b] = new TrieNode();
            node = node.children[b]!;
            node.count += 1;
        }
    };

    const query = (root: TrieNode | null, num: number, limit: number, bit: number): number => {
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

    const countSmallerThan = (limit: number): number => {
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
}
