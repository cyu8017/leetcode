export function minPatches(nums: number[], n: number): number {
    let patches = 0;
    let miss = 1;
    let index = 0;
    while (miss <= n) {
        if (index < nums.length && nums[index] <= miss) {
            miss += nums[index++];
        } else {
            miss += miss;
            patches += 1;
        }
    }
    return patches;
}
