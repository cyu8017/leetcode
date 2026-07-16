// LeetCode 0307 - Range Sum Query - Mutable
// https://leetcode.com/problems/range-sum-query-mutable/

export class NumArray {
    private nums: number[];
    private size: number;
    private tree: number[];
    private add: (index: number, delta: number) => void;

    constructor(nums: number[]) {
        this.nums = nums;
        this.size = nums.length;
        this.tree = Array(this.size + 1).fill(0);
        this.add = (index: number, delta: number) => {
            while (index <= this.size) {
                this.tree[index] += delta;
                index += index & -index;
            }
        };
        for (let index = 0; index < nums.length; index += 1) {
            this.add(index + 1, nums[index]);
        }
    }

    update(index: number, val: number): void {
        const delta = val - this.nums[index];
        this.nums[index] = val;
        this.add(index + 1, delta);
    }

    sumRange(left: number, right: number): number {
        const prefix = (index: number): number => {
            let total = 0;
            while (index > 0) {
                total += this.tree[index];
                index -= index & -index;
            }
            return total;
        };
        return prefix(right + 1) - prefix(left);
    }
}
