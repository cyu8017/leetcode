// LeetCode 0315 - Count of Smaller Numbers After Self
export function countSmaller(nums: number[]): number[] {
    const sorted: number[] = [];
    const result: number[] = [];
    for (let index = nums.length - 1; index >= 0; index -= 1) {
        const num = nums[index];
        let left = 0;
        let right = sorted.length;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (sorted[mid] < num) left = mid + 1;
            else right = mid;
        }
        result.push(left);
        sorted.splice(left, 0, num);
    }
    return result.reverse();
}
