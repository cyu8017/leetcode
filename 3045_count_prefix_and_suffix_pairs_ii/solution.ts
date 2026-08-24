// LeetCode 3045 - Count Prefix and Suffix Pairs II
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

export class Node {
    constructor() {
        this.children = new Map();
        this.cnt = 0;
    }
}
export function countPrefixSuffixPairs(words: any): any {
    const trie = new Node();
    let ans = 0;
    for (const s of words) {
        let node = trie;
        const m = s.length;
        for (let i = 0; i < m; i++) {
            const p = s.charCodeAt(i) * 32 + s.charCodeAt(m - i - 1);
            let next = node.children.get(p);
            if (!next) {
                next = new Node();
                node.children.set(p, next);
            }
            node = next;
            ans += node.cnt;
        }
        node.cnt++;
    }
    return ans;
}
