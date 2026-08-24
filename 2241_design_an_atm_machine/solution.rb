# LeetCode 2241 - Design an ATM Machine
# https://leetcode.com/problems/design-an-atm-machine/

class ATM
  def initialize
    @cnt = [0, 0, 0, 0, 0]
    @vals = [20, 50, 100, 200, 500]
  end

  def deposit(banknotes_count)
    5.times { |i| @cnt[i] += banknotes_count[i] }
    nil
  end

  def withdraw(amount)
    take = [0, 0, 0, 0, 0]
    remain = amount
    tmp = @cnt.dup
    4.downto(0) do |i|
      need = remain / @vals[i]
      need = tmp[i] if need > tmp[i]
      take[i] = need
      remain -= need * @vals[i]
    end
    return [-1] if remain != 0

    5.times { |i| @cnt[i] -= take[i] }
    take
  end
end
