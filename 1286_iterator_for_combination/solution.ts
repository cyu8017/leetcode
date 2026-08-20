// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

function buildCombinations(characters: any, k: any, start: any, path: any, depth: any, out: any): any {
    if (depth === k) {
        out.push(path.join(''));
        return;
    }
    for (let i = start; i < characters.length; i++) {
        path[depth] = characters[i];
        buildCombinations(characters, k, i + 1, path, depth + 1, out);
    }
}

class CombinationIterator {
    items: any;
    index: any;

    constructor(characters: string, combinationLength: number) {
        this.items = [];
        buildCombinations(characters, combinationLength, 0, new Array(combinationLength), 0, this.items);
        this.index = 0;
    }

    next(): string {
        return this.items[this.index++];
    }

    hasNext(): boolean {
        return this.index < this.items.length;
    }
}
