# LeetCode 2299 - Strong Password Checker II
# https://leetcode.com/problems/strong-password-checker-ii/

# @param {String} password
# @return {Boolean}
def strong_password_checker_ii(password)
  return false if password.length < 8

  special = "!@#$%^&*()-+"
  has_lower = has_upper = has_digit = has_special = false
  password.chars.each_with_index do |c, i|
    return false if i > 0 && c == password[i - 1]

    if c >= "a" && c <= "z"
      has_lower = true
    elsif c >= "A" && c <= "Z"
      has_upper = true
    elsif c >= "0" && c <= "9"
      has_digit = true
    elsif special.include?(c)
      has_special = true
    end
  end
  has_lower && has_upper && has_digit && has_special
end
