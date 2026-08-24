// LeetCode 3635 - Earliest Finish Time for Land and Water Rides II
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

export function earliestFinishTime(landStartTime: any, landDuration: any, waterStartTime: any, waterDuration: any): any {
    const calc = (a1, t1, a2, t2) => {
        let minEnd = Infinity;
        for (let i = 0; i < a1.length; i++) minEnd = Math.min(minEnd, a1[i] + t1[i]);
        let ans = Infinity;
        for (let i = 0; i < a2.length; i++) ans = Math.min(ans, Math.max(minEnd, a2[i]) + t2[i]);
        return ans;
    };
    return Math.min(
        calc(landStartTime, landDuration, waterStartTime, waterDuration),
        calc(waterStartTime, waterDuration, landStartTime, landDuration));
}
