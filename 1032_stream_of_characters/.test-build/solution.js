"use strict";
// LeetCode 1032 - Stream of Characters
// https://leetcode.com/problems/stream-of-characters/
Object.defineProperty(exports, "__esModule", { value: true });
exports.StreamChecker = void 0;
class StreamChecker {
    constructor(words) {
        this.trie = {};
        this.stream = [];
        this.trie = {};
        for (const word of words) {
            let node = this.trie;
            for (let i = word.length - 1; i >= 0; i--) {
                const ch = word[i];
                if (!node[ch])
                    node[ch] = {};
                node = node[ch];
            }
            node['$'] = true;
        }
        this.stream = [];
    }
    query(letter) {
        this.stream.push(letter);
        let node = this.trie;
        for (let i = this.stream.length - 1; i >= 0; i--) {
            if (node['$'])
                return true;
            const ch = this.stream[i];
            if (!node[ch])
                return false;
            node = node[ch];
        }
        return !!node['$'];
    }
}
exports.StreamChecker = StreamChecker;
