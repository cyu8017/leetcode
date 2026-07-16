// LeetCode 0126 - Word Ladder II
// https://leetcode.com/problems/word-ladder-ii/

export function findLadders(beginWord: string, endWord: string, wordList: string[]): string[][] {
    const words = new Set(wordList);
    if (!words.has(endWord)) {
        return [];
    }

    const parents = new Map<string, string[]>();
    const visited = new Set([beginWord]);
    let queue = [beginWord];
    let found = false;

    while (queue.length && !found) {
        const levelVisited = new Set<string>();
        const nextQueue: string[] = [];

        for (const word of queue) {
            for (let i = 0; i < word.length; i++) {
                for (let code = 97; code <= 122; code++) {
                    const next = word.slice(0, i) + String.fromCharCode(code) + word.slice(i + 1);
                    if (!words.has(next) || visited.has(next)) {
                        continue;
                    }
                    if (!levelVisited.has(next)) {
                        levelVisited.add(next);
                        nextQueue.push(next);
                    }
                    if (!parents.has(next)) {
                        parents.set(next, []);
                    }
                    parents.get(next)!.push(word);
                    if (next === endWord) {
                        found = true;
                    }
                }
            }
        }

        for (const word of levelVisited) {
            visited.add(word);
        }
        queue = nextQueue;
    }

    if (!found) {
        return [];
    }

    const results: string[][] = [];
    const dfs = (word: string, path: string[]): void => {
        if (word === beginWord) {
            results.push([...path].reverse());
            return;
        }
        for (const parent of parents.get(word)!) {
            path.push(parent);
            dfs(parent, path);
            path.pop();
        }
    };

    dfs(endWord, [endWord]);
    results.sort((a, b) => a.join().localeCompare(b.join()));
    return results;
}