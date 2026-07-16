// LeetCode 0403 - Frog Jump
export function canCross(stones: number[]): boolean {
    const jumps = new Map(stones.map((stone) => [stone, new Set<number>()]));
    jumps.get(0)!.add(0);

    for (const stone of stones) {
        for (const jump of jumps.get(stone)!) {
            for (const nextJump of [jump - 1, jump, jump + 1]) {
                if (nextJump > 0 && jumps.has(stone + nextJump)) {
                    jumps.get(stone + nextJump)!.add(nextJump);
                }
            }
        }
    }

    return jumps.get(stones[stones.length - 1])!.size > 0;
}
