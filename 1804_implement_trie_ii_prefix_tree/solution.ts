// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/

class TrieNode {
    children = new Map<string, TrieNode>();
    wordCount = 0;
    prefixCount = 0;
}

export class Trie {
    private readonly root = new TrieNode();

    insert(word: string): null {
        let node = this.root;
        for (const ch of word) {
            if (!node.children.has(ch)) node.children.set(ch, new TrieNode());
            node = node.children.get(ch)!;
            node.prefixCount += 1;
        }
        node.wordCount += 1;
        return null;
    }

    countWordsEqualTo(word: string): number {
        const node = this.find(word);
        return node ? node.wordCount : 0;
    }

    countWordsStartingWith(prefix: string): number {
        const node = this.find(prefix);
        return node ? node.prefixCount : 0;
    }

    erase(word: string): null {
        let node = this.root;
        for (const ch of word) {
            node = node.children.get(ch)!;
            node.prefixCount -= 1;
        }
        node.wordCount -= 1;
        return null;
    }

    private find(text: string): TrieNode | null {
        let node = this.root;
        for (const ch of text) {
            const next = node.children.get(ch);
            if (!next) return null;
            node = next;
        }
        return node;
    }
}
