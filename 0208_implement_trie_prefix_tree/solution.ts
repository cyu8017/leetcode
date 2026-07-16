// LeetCode 0208 - Implement Trie (Prefix Tree)
// https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode {
    children = new Map<string, TrieNode>();
    isWord = false;
}

export class Trie {
    private readonly root = new TrieNode();

    insert(word: string): null {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char)!;
        }
        node.isWord = true;
        return null;
    }

    search(word: string): boolean {
        const node = this.find(word);
        return node !== null && node.isWord;
    }

    startsWith(prefix: string): boolean {
        return this.find(prefix) !== null;
    }

    private find(text: string): TrieNode | null {
        let node = this.root;
        for (const char of text) {
            const next = node.children.get(char);
            if (!next) return null;
            node = next;
        }
        return node;
    }
}