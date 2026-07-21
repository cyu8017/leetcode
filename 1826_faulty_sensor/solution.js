// LeetCode 1826 - Faulty Sensor
// https://leetcode.com/problems/faulty-sensor/

/**
 * @param {number[]} sensor1
 * @param {number[]} sensor2
 * @return {number}
 */
var badSensor = function(sensor1, sensor2) {
    if (sensor1.every((v, i) => v === sensor2[i])) return -1;

    const isDefective = (correct, faulty) => {
        const n = correct.length;
        let i = 0;
        while (i < n && correct[i] === faulty[i]) i += 1;
        if (i === n) return false;
        let j = i;
        while (j < n - 1 && correct[j + 1] === faulty[j]) j += 1;
        return j === n - 1;
    };

    const sensor1Bad = isDefective(sensor2, sensor1);
    const sensor2Bad = isDefective(sensor1, sensor2);
    if (sensor1Bad && sensor2Bad) return -1;
    if (sensor1Bad) return 1;
    if (sensor2Bad) return 2;
    return -1;
};
