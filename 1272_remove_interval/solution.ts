// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

function removeInterval(intervals: number[][], toBeRemoved: number[]): number[][] {
    const left = toBeRemoved[0];
    const right = toBeRemoved[1];
    const answer = [];
    for (const [start, end] of intervals) {
        if (end <= left || start >= right) {
            answer.push([start, end]);
        } else {
            if (start < left) answer.push([start, left]);
            if (end > right) answer.push([right, end]);
        }
    }
    return answer;
}
