var average = function(salary) {
    let total = 0, minimum = Infinity, maximum = -Infinity;
    for (const value of salary) {
        total += value;
        minimum = Math.min(minimum, value);
        maximum = Math.max(maximum, value);
    }
    return (total - minimum - maximum) / (salary.length - 2);
};
