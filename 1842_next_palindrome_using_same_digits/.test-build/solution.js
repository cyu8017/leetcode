"use strict";
// LeetCode 1842 - Next Palindrome Using Same Digits
// https://leetcode.com/problems/next-palindrome-using-same-digits/
function nextPalindrome(num) {
    const nums = num.split('');
    const nextPermutation = (arr) => {
        const n = Math.floor(arr.length / 2);
        let i = n - 2;
        while (i >= 0 && arr[i] >= arr[i + 1])
            i -= 1;
        if (i < 0)
            return false;
        let j = n - 1;
        while (arr[j] <= arr[i])
            j -= 1;
        [arr[i], arr[j]] = [arr[j], arr[i]];
        const mid = arr.slice(i + 1, n).reverse();
        for (let k = 0; k < mid.length; k++)
            arr[i + 1 + k] = mid[k];
        return true;
    };
    if (!nextPermutation(nums))
        return '';
    const n = nums.length;
    for (let i = 0; i < Math.floor(n / 2); i++)
        nums[n - i - 1] = nums[i];
    return nums.join('');
}
