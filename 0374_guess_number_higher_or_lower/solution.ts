export class Solution {
    guessNumber(n: number): number {
        let left = 1;
        let right = n;
        while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            const result = this.guess(mid);
            if (result === 0) return mid;
            if (result < 0) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    }

    guess(_num: number): number {
        return 0;
    }
}
