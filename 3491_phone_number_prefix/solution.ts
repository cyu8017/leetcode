// LeetCode 3491 - Phone Number Prefix
// https://leetcode.com/problems/phone-number-prefix/

export function phonePrefix(numbers: any): any {
    numbers = numbers.slice().sort();
    for (let i = 0; i + 1 < numbers.length; i++) {
        if (numbers[i].length <= numbers[i + 1].length && numbers[i + 1].startsWith(numbers[i]))
            return false;
    }
    return true;
}
