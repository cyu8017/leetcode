function shuffle(nums: any, n: any): any {
    const result: any[] = [];
    for (let i = 0; i < n; i++) result.push(nums[i], nums[i + n]);
    return result;
}
