// LeetCode 3952 - Maximum Total Value of Covered Indices
// https://leetcode.com/problems/maximum-total-value-of-covered-indices/
var maxTotalValue = function(nums, s) {
        let answer = 0;
        for (let i = 0; i < s.length;) {
            if (s[i] == '0') { i++; continue; }
            let start = i;
            while (i < s.length && s[i] == '1') i++;
            let end = i - 1;
            if (start == 0) {
                for (let index = start; index <= end; index++) answer += nums[index];
                continue;
            }
            let minimum = nums[start - 1];
            let total = 0;
            for (let index = start - 1; index <= end; index++) {
                total += nums[index];
                if (nums[index] < minimum) minimum = nums[index];
            }
            answer += total - minimum;
        }
        return answer;
    
};
