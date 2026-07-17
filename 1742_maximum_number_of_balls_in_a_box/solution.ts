// LeetCode 1742 - Maximum Number of Balls in a Box
// https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

function countBalls(lowLimit: number, highLimit: number): number {
    const counts = new Map<number, number>();
    for (let value = lowLimit; value <= highLimit; value++) {
        let box = 0;
        let v = value;
        while (v > 0) {
            box += v % 10;
            v = Math.floor(v / 10);
        }
        counts.set(box, (counts.get(box) || 0) + 1);
    }
    return Math.max(...counts.values());
}
