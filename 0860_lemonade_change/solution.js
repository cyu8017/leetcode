// LeetCode 0860 - Lemonade Change
// https://leetcode.com/problems/lemonade-change/

/**
 * @param {number[]} bills
 * @return {boolean}
 */
var lemonadeChange = function(bills) {
    let fives = 0, tens = 0;
    for (const bill of bills) {
        if (bill === 5) fives++;
        else if (bill === 10) {
            if (fives === 0) return false;
            fives--;
            tens++;
        } else {
            if (tens > 0 && fives > 0) { tens--; fives--; }
            else if (fives >= 3) fives -= 3;
            else return false;
        }
    }
    return true;
};
