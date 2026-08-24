// LeetCode 0818 - Race Car
// https://leetcode.com/problems/race-car/

export function racecar(target: number): number {
    const key = (pos, speed) => (pos * 1048576) ^ (speed & 0xfffff);
    const queue = [[0, 1, 0]];
    const seen = new Set([key(0, 1)]);
    while (queue.length) {
        const [pos, speed, steps] = queue.shift();
        if (pos === target) return steps;
        const nxtPos = pos + speed, nxtSpeed = speed * 2;
        if (!seen.has(key(nxtPos, nxtSpeed)) && Math.abs(nxtPos) < target * 2) {
            seen.add(key(nxtPos, nxtSpeed));
            queue.push([nxtPos, nxtSpeed, steps + 1]);
        }
        const revSpeed = speed > 0 ? -1 : 1;
        if (!seen.has(key(pos, revSpeed))) {
            seen.add(key(pos, revSpeed));
            queue.push([pos, revSpeed, steps + 1]);
        }
    }
    return -1;
}
