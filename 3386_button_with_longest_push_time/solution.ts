// LeetCode 3386 - Button with Longest Push Time
// https://leetcode.com/problems/button-with-longest-push-time/

export function buttonWithLongestTime(events: any): any {
    let bestT = events[0][1], bestI = events[0][0];
    for (let i = 1; i < events.length; i++) {
        const t = events[i][1] - events[i - 1][1];
        if (t > bestT || (t === bestT && events[i][0] < bestI)) {
            bestT = t;
            bestI = events[i][0];
        }
    }
    return bestI;
}
