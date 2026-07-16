// LeetCode 0164 - Maximum Gap
// https://leetcode.com/problems/maximum-gap/

export function maximumGap(nums: number[]): number {
    if (nums.length < 2) {
        return 0;
    }

    const low = Math.min(...nums);
    const high = Math.max(...nums);
    if (low === high) {
        return 0;
    }

    const bucketSize = Math.max(1, Math.floor((high - low) / (nums.length - 1)));
    const bucketCount = Math.floor((high - low) / bucketSize) + 1;
    const minimums = Array<number>(bucketCount).fill(Infinity);
    const maximums = Array<number>(bucketCount).fill(-Infinity);
    const used = Array<boolean>(bucketCount).fill(false);

    for (const number of nums) {
        const index = Math.floor((number - low) / bucketSize);
        used[index] = true;
        minimums[index] = Math.min(minimums[index], number);
        maximums[index] = Math.max(maximums[index], number);
    }

    let best = 0;
    let previousMaximum = low;
    for (let index = 0; index < bucketCount; index++) {
        if (!used[index]) {
            continue;
        }
        best = Math.max(best, minimums[index] - previousMaximum);
        previousMaximum = maximums[index];
    }
    return best;
}