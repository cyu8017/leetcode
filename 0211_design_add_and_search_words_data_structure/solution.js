// LeetCode 0211 - Design Add and Search Words Data Structure
// https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode {
    constructor() {
        this.children = new Map();
        this.isWord = false;
    }
}

class WordDictionary {
    constructor() {
        this.root = new TrieNode();
    }

    /**
     * @param {string} word
     * @return {null}
     */
    addWord(word) {
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
        const dfs = (node, index) => {
            if (index === word.length) {
                return node.isWord;
            }
            const char = word[index];
            if (char === ".") {
                for (const child of node.children.values()) {
                    if (dfs(child, index + 1)) {
                        return true;
                    }
                }
                return false;
            }
            if (!node.children.has(char)) {
                return false;
            }
            return dfs(node.children.get(char), index + 1);
        };
        return dfs(this.root, 0);
    }
}

module.exports = { WordDictionary };
