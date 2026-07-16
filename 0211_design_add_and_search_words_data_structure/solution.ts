// LeetCode 0211 - Design Add and Search Words Data Structure
// https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode {
    children = new Map<string, TrieNode>();
    isWord = false;
}

export class WordDictionary {
    private readonly root = new TrieNode();

    addWord(word: string): null {
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
        const dfs = (node: TrieNode, index: number): boolean => {
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
            const next = node.children.get(char);
            if (!next) {
                return false;
            }
            return dfs(next, index + 1);
        };
        return dfs(this.root, 0);
    }
}
