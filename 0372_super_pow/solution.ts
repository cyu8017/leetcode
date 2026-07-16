export function superPow(a: number, b: number[]): number {
    const mod = 1337;
    a %= mod;

    const powMod = (base: number, exponent: number): number => {
        let result = 1;
        while (exponent > 0) {
            if (exponent & 1) result = (result * base) % mod;
            base = (base * base) % mod;
            exponent >>= 1;
        }
        return result;
    };

    let result = 1;
    for (const digit of b) {
        result = (powMod(result, 10) * powMod(a, digit)) % mod;
    }
    return result;
}
