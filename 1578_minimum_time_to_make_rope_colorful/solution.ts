// LeetCode 1578 - Minimum Time to Make Rope Colorful
// https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
// @ts-nocheck

function minCost(colors: string, neededTime: number[]): number {
    let answer = 0, maximum = 0;
    for (let i = 0; i < neededTime.length; i++) {
        if (i && colors[i] !== colors[i - 1]) maximum = 0;
        answer += Math.min(maximum, neededTime[i]);
        maximum = Math.max(maximum, neededTime[i]);
    }
    return answer;
}
