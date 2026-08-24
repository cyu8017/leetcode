// LeetCode 4006 - Count Valid Prefixes
// https://leetcode.com/problems/count-valid-prefixes/
var countValidPrefixes = function(s) {
        let ans = 0, t = 0;
        for (let i = 0; i < s.length; i++) {
            if (s[i] == '1') t++;
            else t--;
            if (t >= -1 && t <= 1) ans++;
        }
        return ans;
    
};
