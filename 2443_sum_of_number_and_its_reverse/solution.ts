// LeetCode 2443 - Sum of Number and Its Reverse
// https://leetcode.com/problems/sum-of-number-and-its-reverse/

export function sumOfNumberAndReverse(num: number): boolean {
    const rev = (x) => {
        let r = 0;
        while (x > 0) {
            r = r * 10 + x % 10;
            x = Math.floor(x / 10);
        }
        return r;
    };
    for (let i = 0; i <= num; i++) {
        if (i + rev(i) === num) return true;
    }
    return false;
}
