// LeetCode 0401 - Binary Watch
var readBinaryWatch = function (turnedOn) {
    const result = [];
    const bitCount = (value) => value.toString(2).split("1").length - 1;
    for (let hour = 0; hour < 12; hour += 1) {
        for (let minute = 0; minute < 60; minute += 1) {
            if (bitCount(hour) + bitCount(minute) === turnedOn) {
                result.push(`${hour}:${String(minute).padStart(2, "0")}`);
            }
        }
    }
    return result;
};

module.exports = { readBinaryWatch };
