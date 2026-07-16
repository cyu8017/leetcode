// LeetCode 0393 - UTF-8 Validation
var validUtf8 = function (data) {
    let remaining = 0;

    for (let byte of data) {
        byte &= 0xff;
        if (remaining === 0) {
            if (byte >> 7 === 0b0) continue;
            if (byte >> 5 === 0b110) remaining = 1;
            else if (byte >> 4 === 0b1110) remaining = 2;
            else if (byte >> 3 === 0b11110) remaining = 3;
            else return false;
        } else {
            if (byte >> 6 !== 0b10) return false;
            remaining -= 1;
        }
    }

    return remaining === 0;
};

module.exports = { validUtf8 };
