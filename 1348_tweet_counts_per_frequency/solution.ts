// LeetCode 1348 - Tweet Counts Per Frequency
// https://leetcode.com/problems/tweet-counts-per-frequency/

class TweetCounts {
    times: any;
    constructor() {

        this.times = new Map();
    }
    recordTweet(tweetName: string, time: number): void {

        if (!this.times.has(tweetName)) this.times.set(tweetName, []);
        const arr = this.times.get(tweetName);
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] < time) lo = mid + 1;
            else hi = mid;
        }
        arr.splice(lo, 0, time);
    }
    getTweetCountsPerFrequency(freq: string, tweetName: string, startTime: number, endTime: number): number[] {

        const size = ({ minute: 60, hour: 3600, day: 86400 } as Record<string, number>)[freq]!;
        const times = this.times.get(tweetName) || [];
        const answer: any[] = [];
        const lower = (x: any): any => {
            let lo = 0, hi = times.length;
            while (lo < hi) {
                const mid = (lo + hi) >> 1;
                if (times[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            return lo;
        };
        const upper = (x: any): any => {
            let lo = 0, hi = times.length;
            while (lo < hi) {
                const mid = (lo + hi) >> 1;
                if (times[mid] <= x) lo = mid + 1;
                else hi = mid;
            }
            return lo;
        };
        for (let start = startTime; start <= endTime; start += size) {
            const end = Math.min(endTime, start + size - 1);
            answer.push(upper(end) - lower(start));
        }
        return answer;
    }
}
