// LeetCode 3986 - Number of Elapsed Seconds Between Two Times
// https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/

export function toSeconds(s: any): any {
        let h = (s[0] - '0') * 10 + (s[1] - '0');
        let m = (s[3] - '0') * 10 + (s[4] - '0');
        let sec = (s[6] - '0') * 10 + (s[7] - '0');
        return h * 3600 + m * 60 + sec;
    
}export function secondsBetweenTimes(startTime: any, endTime: any): any {
        return toSeconds(endTime) - toSeconds(startTime);
    
}
