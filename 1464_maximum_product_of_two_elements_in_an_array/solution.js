var maxProduct = function(nums) {
    let first = 0, second = 0;
    for (const value of nums) {
        if (value >= first) [first, second] = [value, first];
        else if (value > second) second = value;
    }
    return (first - 1) * (second - 1);
};
