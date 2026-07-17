# LeetCode 1797 - Design Authentication Manager
# https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager
  # @param {Integer} time_to_live
  def initialize(time_to_live)
    @ttl = time_to_live
    @tokens = {}
  end

  # @param {String} token_id
  # @param {Integer} current_time
  # @return {Void}
  def generate(token_id, current_time)
    @tokens[token_id] = current_time + @ttl
    nil
  end

  # @param {String} token_id
  # @param {Integer} current_time
  # @return {Void}
  def renew(token_id, current_time)
    if @tokens.key?(token_id) && @tokens[token_id] > current_time
      @tokens[token_id] = current_time + @ttl
    end
    nil
  end

  # @param {Integer} current_time
  # @return {Integer}
  def count_unexpired_tokens(current_time)
    @tokens.values.count { |exp| exp > current_time }
  end
end
