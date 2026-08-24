// LeetCode 0739 - Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/

export function dailyTemperatures(temperatures: number[]): number[] {
    const answer = new Array(temperatures.length).fill(0);
    const stack = [];
    for (let i = 0; i < temperatures.length; i++) {
        while (stack.length > 0 && temperatures[stack[stack.length - 1]] < temperatures[i]) {
            const prev = stack.pop();
            answer[prev] = i - prev;
        }
        stack.push(i);
    }
    return answer;
}
