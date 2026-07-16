// LeetCode 0208 - Implement Trie (Prefix Tree)
// https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode {
    constructor() {
        this.children = new Map();
        this.isWord = false;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    /**
     * @param {string} word
     * @return {null}
     */
    insert(word) {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char);
        }
        node.isWord = true;
        return null;
    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    search(word) {
        const node = this.find(word);
        return node !== null && node.isWord;
    }

    /**
     * @param {string} prefix
     * @return {boolean}
     */
    startsWith(prefix) {
        return this.find(prefix) !== null;
    }

    /**
     * @param {string} text
     * @return {TrieNode|null}
     */
    find(text) {
        let node = this.root;
        for (const char of text) {
            if (!node.children.has(char)) return null;
            node = node.children.get(char);
        }
        return node;
    }
}

module.exports = { Trie };