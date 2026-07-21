"use strict";
// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/
Object.defineProperty(exports, "__esModule", { value: true });
exports.Trie = void 0;
class TrieNode {
    constructor() {
        this.children = new Map();
        this.wordCount = 0;
        this.prefixCount = 0;
    }
}
class Trie {
    constructor() {
        this.root = new TrieNode();
    }
    insert(word) {
        let node = this.root;
        for (const ch of word) {
            if (!node.children.has(ch))
                node.children.set(ch, new TrieNode());
            node = node.children.get(ch);
            node.prefixCount += 1;
        }
        node.wordCount += 1;
        return null;
    }
    countWordsEqualTo(word) {
        const node = this.find(word);
        return node ? node.wordCount : 0;
    }
    countWordsStartingWith(prefix) {
        const node = this.find(prefix);
        return node ? node.prefixCount : 0;
    }
    erase(word) {
        let node = this.root;
        for (const ch of word) {
            node = node.children.get(ch);
            node.prefixCount -= 1;
        }
        node.wordCount -= 1;
        return null;
    }
    find(text) {
        let node = this.root;
        for (const ch of text) {
            const next = node.children.get(ch);
            if (!next)
                return null;
            node = next;
        }
        return node;
    }
}
exports.Trie = Trie;
