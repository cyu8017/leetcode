// LeetCode 2678 - Number of Senior Citizens
// https://leetcode.com/problems/number-of-senior-citizens/

var countSeniors = function(details) {
    let ans = 0;
    for (const d of details) {
        const age = (d.charCodeAt(11) - 48) * 10 + (d.charCodeAt(12) - 48);
        if (age > 60) ans++;
    }
    return ans;
};
