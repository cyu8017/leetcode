// LeetCode 0127 - Word Ladder
// https://leetcode.com/problems/word-ladder/

export function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {
    const words = new Set(wordList);
    if (!words.has(endWord)) {
        return 0;
    }

    const queue: Array<[string, number]> = [[beginWord, 1]];
    const visited = new Set([beginWord]);
    let front = 0;

    while (front < queue.length) {
        const [word, steps] = queue[front++];
        if (word === endWord) {
            return steps;
        }

        for (let i = 0; i < word.length; i++) {
            for (let code = 97; code <= 122; code++) {
                const next = word.slice(0, i) + String.fromCharCode(code) + word.slice(i + 1);
                if (words.has(next) && !visited.has(next)) {
                    visited.add(next);
                    queue.push([next, steps + 1]);
                }
            }
        }
    }

    return 0;
}