export function maxEnvelopes(envelopes: number[][]): number {
    envelopes.sort((a, b) => (a[0] === b[0] ? b[1] - a[1] : a[0] - b[0]));
    const tails: number[] = [];

    for (const [, height] of envelopes) {
        let left = 0;
        let right = tails.length;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (tails[mid] < height) left = mid + 1;
            else right = mid;
        }
        if (left === tails.length) tails.push(height);
        else tails[left] = height;
    }

    return tails.length;
}
