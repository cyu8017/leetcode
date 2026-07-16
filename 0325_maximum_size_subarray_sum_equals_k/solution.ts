export function maxSubArrayLen(nums: number[], k: number): number {
    const prefixIndex = new Map<number, number>([[0, -1]]);
    let prefix = 0;
    let best = 0;
    for (let index = 0; index < nums.length; index += 1) {
        prefix += nums[index];
        if (prefixIndex.has(prefix - k)) best = Math.max(best, index - (prefixIndex.get(prefix - k) as number));
        if (!prefixIndex.has(prefix)) prefixIndex.set(prefix, index);
    }
    return best;
}
