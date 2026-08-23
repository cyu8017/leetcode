// LeetCode 3998 - Transform Binary String Using Subsequence Sort
// https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/
var transformStr = function(s, strs) {
        let n = s.length;
        let prefix = new Array(n + 1).fill(0);
        for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + (s[i] == '1' ? 1 : 0);
        let result = new Array(strs.length).fill(false);
        for (let i = 0; i < strs.length; i++) {
            let left = 0, right = 0;
            let ok = true;
            for (let j = 0; j < n; j++) {
                left += (strs[i][j] == '1' ? 1 : 0);
                let add = (strs[i][j] != '0' ? 1 : 0);
                right = right + add;
                if (right > prefix[j + 1]) right = prefix[j + 1];
                if (left > right) {
                    ok = false;
                    break;
                }
            }
            result[i] = ok && left <= prefix[n] && prefix[n] <= right;
        }
        return result;
    
};
