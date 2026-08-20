// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

function beforeAndAfterPuzzles(phrases: string[]): string[] {
    const split = phrases.map((p) => p.split(' '));
    const result = new Set();
    for (let i = 0; i < split.length; i++) {
        for (let j = 0; j < split.length; j++) {
            if (i === j) continue;
            if (split[i][split[i].length - 1] === split[j][0]) {
                result.add([...split[i], ...split[j].slice(1)].join(' '));
            }
        }
    }
    return [...result].sort();
}
