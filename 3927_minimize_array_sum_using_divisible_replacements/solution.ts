// LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
// https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

export function minArraySum(nums: any): any {
        let maximum = 0;
        let present = new Array(100001).fill(false);
        for (const value of nums) {
            present[value] = true;
            if (value > maximum) maximum = value;
        }
        let best = new Array(maximum + 1).fill(0);
        for (let divisor = 1; divisor <= maximum; divisor++) {
            if (!present[divisor]) continue;
            for (let multiple = divisor; multiple <= maximum; multiple += divisor) {
                if (best[multiple] == 0) best[multiple] = divisor;
            }
        }
        let answer = 0;
        for (const value of nums) answer += best[value];
        return answer;
    
}
