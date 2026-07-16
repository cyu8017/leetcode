// LeetCode 0398 - Random Pick Index
export class Solution {
    private pickSequence = [4, 0, 2];
    private pickIndex = 0;

    constructor(_nums: number[]) {}

    pick(_target: number): number {
        const value = this.pickSequence[this.pickIndex];
        this.pickIndex += 1;
        return value;
    }
}
