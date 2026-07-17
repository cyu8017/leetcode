// LeetCode 1788 - Maximize the Beauty of the Garden
// https://leetcode.com/problems/maximize-the-beauty-of-the-garden/

function maximumBeauty(flowers: number[]): number {
    const first = new Map<number, number>();
    const prefix = [0];
    for (const value of flowers) {
        prefix.push(prefix[prefix.length - 1] + Math.max(value, 0));
    }
    let best = -Infinity;
    for (let i = 0; i < flowers.length; i++) {
        const value = flowers[i];
        if (first.has(value)) {
            const left = first.get(value)!;
            const between = prefix[i] - prefix[left + 1];
            best = Math.max(best, flowers[left] + flowers[i] + between);
        } else {
            first.set(value, i);
        }
    }
    return best;
}
