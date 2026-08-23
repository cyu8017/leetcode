// LeetCode 3783 - Mirror Distance Of An Integer
// https://leetcode.com/problems/mirror_distance_of_an_integer/

var mirrorDistance = function(n) {
    const reverse = (x) => {
        let y = 0;
        for (; x > 0; x = Math.floor(x / 10)) y = y * 10 + x % 10;
        return y;
    };
    return Math.abs(n - reverse(n));
};
