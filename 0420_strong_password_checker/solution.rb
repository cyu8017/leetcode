# LeetCode 0420 - Strong Password Checker
# https://leetcode.com/problems/strong-password-checker/

class Solution
  def strong_password_checker(password)
    length = password.length
    missing = 3
    missing -= 1 if password.match?(/[a-z]/)
    missing -= 1 if password.match?(/[A-Z]/)
    missing -= 1 if password.match?(/\d/)

    replace = 0
    one_repeat = 0
    two_repeat = 0
    index = 0
    while index < length
      run = 1
      while index + run < length && password[index + run] == password[index]
        run += 1
      end
      if run >= 3
        replace += run / 3
        one_repeat += 1 if run % 3 == 0
        two_repeat += 1 if run % 3 == 1
      end
      index += run
    end

    return [6 - length, missing].max if length < 6
    return [missing, replace].max if length <= 20

    delete = length - 20
    replace -= [delete, one_repeat].min
    delete -= [delete, one_repeat].min
    replace -= [delete / 2, two_repeat].min
    delete -= [delete / 2, two_repeat].min * 2
    replace -= delete / 3
    length - 20 + [missing, replace].max
  end

  alias_method :strongPasswordChecker, :strong_password_checker
end
