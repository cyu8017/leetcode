// LeetCode 1390: Four Divisors

var sumFourDivisors = function(nums) {
    let total = 0;
    for (const value of nums) {
        let count = 0, sum = 0;
        for (let divisor = 1; divisor * divisor <= value; divisor++) if (value % divisor === 0) {
            count++; sum += divisor;
            if (divisor * divisor !== value) { count++; sum += value / divisor; }
        }
        if (count === 4) total += sum;
    }
    return total;
};
