// LeetCode 3961 - Maximize Sum Of Device Ratings
// https://leetcode.com/problems/maximize-sum-of-device-ratings/

export function maxRatings(units: any): any {
        let n = units[0].length;
        if (n == 1) {
            let ans = 0;
            for (const x of units) ans += x[0];
            return ans;
        }
        let answer = 0;
        let mn = 2147483647, mn2 = 2147483647;
        for (const x of units) {
            x.sort((a,b)=>a-b);
            answer += x[1];
            mn2 = Math.min(mn2, x[1]);
            mn = Math.min(mn, x[0]);
        }
        return answer - (mn2 - mn);
    
}
