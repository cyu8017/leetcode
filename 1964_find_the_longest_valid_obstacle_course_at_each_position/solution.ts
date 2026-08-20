// LeetCode 1964 - Find the Longest Valid Obstacle Course at Each Position
// https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

function longestObstacleCourseAtEachPosition(obstacles: number[]): number[] {
    const tails = [];
    const ans = [];
    for (const x of obstacles) {
        let lo = 0, hi = tails.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (tails[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        if (lo === tails.length) tails.push(x);
        else tails[lo] = x;
        ans.push(lo + 1);
    }
    return ans;
}
