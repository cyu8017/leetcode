var numSubseq = function(nums, target) {
    const mod = 1000000007;
    nums.sort((a, b) => a - b);
    const powers = [1];
    for (let i = 1; i < nums.length; i++) powers.push((powers[i - 1] * 2) % mod);
    let left = 0, right = nums.length - 1, answer = 0;
    while (left <= right) {
        if (nums[left] + nums[right] <= target) answer = (answer + powers[right - left++]) % mod;
        else right--;
    }
    return answer;
};
