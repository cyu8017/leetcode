// LeetCode 3093 - Longest Common Suffix Queries
// https://leetcode.com/problems/longest-common-suffix-queries/

/**
 * @param {string[]} wordsContainer
 * @param {string[]} wordsQuery
 * @return {number[]}
 */
var stringIndices = function(wordsContainer, wordsQuery) {
    const INF = 1 << 30;
    function Trie() {
        this.children = new Array(26).fill(null);
        this.length = INF;
        this.idx = INF;
    }
    const insert = (t, w, i) => {
        let node = t;
        if (node.length > w.length) {
            node.length = w.length;
            node.idx = i;
        }
        for (let k = w.length - 1; k >= 0; k--) {
            const id = w.charCodeAt(k) - 97;
            if (!node.children[id]) node.children[id] = new Trie();
            node = node.children[id];
            if (node.length > w.length) {
                node.length = w.length;
                node.idx = i;
            }
        }
    };
    const query = (t, w) => {
        let node = t;
        for (let k = w.length - 1; k >= 0; k--) {
            const id = w.charCodeAt(k) - 97;
            if (!node.children[id]) break;
            node = node.children[id];
        }
        return node.idx;
    };
    const trie = new Trie();
    for (let i = 0; i < wordsContainer.length; i++) insert(trie, wordsContainer[i], i);
    const ans = new Array(wordsQuery.length);
    for (let i = 0; i < wordsQuery.length; i++) ans[i] = query(trie, wordsQuery[i]);
    return ans;
};
