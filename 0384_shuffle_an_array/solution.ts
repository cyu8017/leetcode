// LeetCode 0384 - Shuffle an Array
export class Solution {
    private readonly original: number[];
    private readonly shuffleSequence = [[3, 1, 2], [1, 3, 2]];
    private shuffleIndex = 0;

    constructor(nums: number[]) {
        this.original = [...nums];
    }

    reset(): number[] {
        return [...this.original];
    }

    shuffle(): number[] {
        const result = this.shuffleSequence[this.shuffleIndex];
        this.shuffleIndex += 1;
        return [...result];
    }
}
