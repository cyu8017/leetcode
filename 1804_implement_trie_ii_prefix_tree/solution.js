// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/

class TrieNode {
    constructor() {
        this.children = {};
        this.wordCount = 0;
        this.prefixCount = 0;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    /**
     * @param {string} word
     * @return {void}
     */
    insert(word) {
        let node = this.root;
        for (const ch of word) {
            if (!node.children[ch]) node.children[ch] = new TrieNode();
            node = node.children[ch];
            node.prefixCount += 1;
        }
        node.wordCount += 1;
    }

    /**
     * @param {string} word
     * @return {number}
     */
    countWordsEqualTo(word) {
        const node = this._find(word);
        return node ? node.wordCount : 0;
    }

    /**
     * @param {string} prefix
     * @return {number}
     */
    countWordsStartingWith(prefix) {
        const node = this._find(prefix);
        return node ? node.prefixCount : 0;
    }

    /**
     * @param {string} word
     * @return {void}
     */
    erase(word) {
        let node = this.root;
        for (const ch of word) {
            node = node.children[ch];
            node.prefixCount -= 1;
        }
        node.wordCount -= 1;
    }

    _find(text) {
        let node = this.root;
        for (const ch of text) {
            if (!node.children[ch]) return null;
            node = node.children[ch];
        }
        return node;
    }
}

module.exports = { Trie };
