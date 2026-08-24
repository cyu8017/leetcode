// LeetCode 3648 - Minimum Sensors to Cover Grid
// https://leetcode.com/problems/minimum-sensors-to-cover-grid/

export function minSensors(n: any, m: any, k: any): any {
    const cover = 2 * k + 1;
    return Math.ceil(n / cover) * Math.ceil(m / cover);
}
