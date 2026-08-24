// LeetCode 3959 - Check Good Integer
// https://leetcode.com/problems/check-good-integer/
var checkGoodInteger = function(n) {
        let s = 0;
        for (; n > 0; n /= 10) {
            let x = n % 10;
            s += x * (x - 1);
        }
        return s >= 50;
    
};
