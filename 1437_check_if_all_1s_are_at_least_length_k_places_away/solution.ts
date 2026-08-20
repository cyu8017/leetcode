function kLengthApart(nums: any, k: any): any {
    let previous = -k - 1;
    for (let i = 0; i < nums.length; i++) if (nums[i]) { if (i - previous <= k) return false; previous = i; }
    return true;
}
