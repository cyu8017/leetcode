function longestSubarray(nums: any): any {
    let left = 0, zeros = 0, best = 0;
    for (let right = 0; right < nums.length; right++) {
        if (nums[right] === 0) zeros++;
        while (zeros > 1) if (nums[left++] === 0) zeros--;
        best = Math.max(best, right - left);
    }
    return best;
}
