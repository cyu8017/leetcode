// LeetCode 1769 - Minimum Number of Operations to Move All Balls to Each Box
// https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

function minOperations(boxes: string): number[] {
    const n = boxes.length;
    const ans: number[] = new Array(n).fill(0);
    let balls = 0;
    let ops = 0;
    for (let i = 1; i < n; i++) {
        balls += Number(boxes[i - 1]);
        ops += balls;
        ans[i] = ops;
    }
    balls = 0;
    ops = 0;
    for (let i = n - 2; i >= 0; i--) {
        balls += Number(boxes[i + 1]);
        ops += balls;
        ans[i] += ops;
    }
    return ans;
}
