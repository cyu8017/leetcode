export function countBits(n: number): number[] {
    const result = new Array<number>(n + 1).fill(0);
    for (let index = 1; index <= n; index += 1) {
        result[index] = result[index & (index - 1)] + 1;
    }
    return result;
}
