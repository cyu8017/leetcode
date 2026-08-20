function canArrange(arr: any, k: any): any {
    const count = Array(k).fill(0);
    for (const value of arr) count[((value % k) + k) % k]++;
    if (count[0] % 2) return false;
    for (let remainder = 1; remainder < k; remainder++) {
        if (count[remainder] !== count[k - remainder]) return false;
    }
    return true;
}
