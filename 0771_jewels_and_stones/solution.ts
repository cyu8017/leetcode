// LeetCode 0771 - Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/

export function numJewelsInStones(jewels: string, stones: string): number {
    const jewelSet = new Set(jewels);
    let count = 0;
    for (const stone of stones) if (jewelSet.has(stone)) count++;
    return count;
}
