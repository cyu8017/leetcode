// LeetCode 1776 - Car Fleet II
// https://leetcode.com/problems/car-fleet-ii/

function getCollisionTimes(cars: number[][]): number[] {
    const n = cars.length;
    const ans: number[] = new Array(n).fill(-1.0);
    const stack: number[] = [];
    for (let i = n - 1; i >= 0; i--) {
        const [pos, speed] = cars[i];
        while (stack.length > 0) {
            const j = stack[stack.length - 1];
            if (speed <= cars[j][1]) {
                stack.pop();
                continue;
            }
            const t = (cars[j][0] - pos) / (speed - cars[j][1]);
            if (ans[j] < 0 || t <= ans[j]) {
                ans[i] = t;
                break;
            }
            stack.pop();
        }
        stack.push(i);
    }
    return ans;
}
